from fastapi import FastAPI,HTTPException,Request,Depends,Header
from fastapi.responses import JSONResponse,Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel,Field,ConfigDict,field_validator
from typing import Literal
from pathlib import Path
from contextlib import asynccontextmanager
import secrets,time,json,datetime,csv,io,os,re
import db,security,ai

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def uid():return secrets.token_hex(16)
@asynccontextmanager
async def lifespan(app):db.init();yield
app=FastAPI(title='StitchLedger API',version='0.2.0',lifespan=lifespan)
@app.middleware('http')
async def guard(request:Request,call_next):
 request.state.request_id=uid()
 if request.url.path.startswith('/api/'):
  size=request.headers.get('content-length','0')
  if not size.isdigit() or int(size)>32768:return JSONResponse({'detail':'Request too large'},413)
  if request.method in ['POST','PUT','PATCH','DELETE']:
   # Read before parsing to enforce the limit even for chunked requests.
   body=b''
   async for chunk in request.stream():
    body+=chunk
    if len(body)>32768:return JSONResponse({'detail':'Request too large'},413)
   request._body=body
  peer=request.client.host if request.client else 'unknown'
  auth=request.url.path in ['/api/auth/register','/api/auth/login','/api/auth/demo']
  if security.limited(('http',peer,auth),20 if auth else 240):return JSONResponse({'detail':'Too many requests. Wait one minute.'},429,headers={'Retry-After':'60'})
 r=await call_next(request);r.headers['X-Request-ID']=request.state.request_id;r.headers['X-Content-Type-Options']='nosniff';r.headers['Referrer-Policy']='no-referrer';r.headers['Content-Security-Policy']="object-src 'none'; base-uri 'self'"
 if request.url.path.startswith('/api/'):r.headers['Cache-Control']='no-store'
 return r
class Model(BaseModel):model_config=ConfigDict(extra='forbid',str_strip_whitespace=True)
class Credentials(Model):
 email:str=Field(min_length=3,max_length=254)
 password:str=Field(min_length=12,max_length=128)
 @field_validator('email')
 @classmethod
 def email_valid(cls,v):
  if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',v):raise ValueError('Enter a valid email address')
  return v.lower()
 @field_validator('password',mode='before')
 @classmethod
 def no_password_whitespace_change(cls,v):
  if isinstance(v,str) and v!=v.strip():raise ValueError('Do not start or end your password with spaces')
  return v
class Register(Credentials):studio:str=Field(min_length=2,max_length=80)
class OrderInput(Model):
 customer:str=Field(min_length=1,max_length=80)
 garment:str=Field(min_length=1,max_length=160)
 due:datetime.date
 total:int=Field(strict=True,ge=0,le=100000000)
 notes:str=Field(default='',max_length=1000)
class CreateOrder(OrderInput):deposit:int=Field(default=0,strict=True,ge=0,le=100000000)
class EditOrder(OrderInput):version:int=Field(strict=True,ge=1)
class ChangeStatus(Model):status:Literal['Booked','Cutting','Sewing','Ready','Collected','Cancelled'];version:int=Field(strict=True,ge=1)
class Payment(Model):
 amount:int=Field(strict=True,gt=0,le=100000000)
 kind:Literal['receipt','refund']='receipt'
 method:Literal['Cash','MoMo','Bank']='Cash'
 note:str=Field(min_length=1,max_length=200)
class Consent(Model):consent:Literal[True]
class DeleteAccount(Model):password:str=Field(min_length=1,max_length=128);confirmation:Literal['DELETE']

def session(c,user):
 token=secrets.token_urlsafe(48);c.execute('INSERT INTO sessions VALUES(?,?,?)',(security.digest(token),user['id'],int(time.time())+43200));return {'token':token,'user':{k:user[k] for k in ['id','email','studio','demo']},'expires_in':43200}
def auth(request:Request):
 value=request.headers.get('authorization','')
 if not value.startswith('Bearer '):raise HTTPException(401,'Sign in to continue')
 token=value[7:]
 with db.read() as c:r=c.execute('SELECT u.* FROM users u JOIN sessions s ON s.user_id=u.id WHERE s.token_hash=? AND s.expires>?',(security.digest(token),int(time.time()))).fetchone()
 if not r:raise HTTPException(401,'Session expired. Sign in again.')
 return dict(r)
def find(c,u,oid):
 r=db.order(c,u['id'],oid)
 if not r:raise HTTPException(404,'Order not found')
 return dict(r)
def audit(c,u,oid,action,detail):c.execute('INSERT INTO audit VALUES(?,?,?,?,?,?)',(uid(),u['id'],oid,action,detail,now()))
def event(c,u,oid,amount,method,note):c.execute('INSERT INTO payments VALUES(?,?,?,?,?,?,?)',(uid(),u['id'],oid,amount,method,note,now()))
def mutable(o):
 if o['status'] in ['Collected','Cancelled']:raise HTTPException(409,'This order is closed. Its records cannot be changed.')
def version(o,v):
 if o['version']!=v:raise HTTPException(409,'Order changed on another device. Refresh and try again.')
def operation(c,u,key,payload,fn):
 if not re.fullmatch(r'[A-Za-z0-9_-]{16,100}',key):raise HTTPException(400,'A valid Idempotency-Key is required')
 dig=security.digest(json.dumps(payload,sort_keys=True,default=str));r=c.execute('SELECT * FROM operations WHERE owner=? AND key=?',(u['id'],key)).fetchone()
 if r:
  if r['digest']!=dig:raise HTTPException(409,'This request key was already used for different data.')
  return json.loads(r['result'])
 out=fn();c.execute('INSERT INTO operations VALUES(?,?,?,?)',(u['id'],key,dig,json.dumps(out)));return out
@app.get('/api/health')
def health():return {'status':'ok','version':'0.2.0'}
@app.post('/api/auth/register',status_code=201)
def register(d:Register):
 hashed=security.password_hash(d.password)
 with db.transaction() as c:
  if c.execute('SELECT 1 FROM users WHERE email=?',(d.email,)).fetchone():raise HTTPException(409,'Unable to register. Try signing in or use another email.')
  u={'id':uid(),'email':d.email,'password':hashed,'studio':d.studio,'demo':0};c.execute('INSERT INTO users VALUES(?,?,?,?,?,?)',(*u.values(),now()));return session(c,u)
@app.post('/api/auth/login')
def login(d:Credentials):
 with db.read() as c:r=c.execute('SELECT * FROM users WHERE email=?',(d.email,)).fetchone()
 if not r:
  security.password_hash(d.password);raise HTTPException(401,'Email or password is incorrect')
 if not security.verify(d.password,r['password']):raise HTTPException(401,'Email or password is incorrect')
 with db.transaction() as c:return session(c,dict(r))
@app.post('/api/auth/logout',status_code=204)
def logout(request:Request,u=Depends(auth)):
 with db.transaction() as c:c.execute('DELETE FROM sessions WHERE token_hash=?',(security.digest(request.headers['authorization'][7:]),))
 return Response(status_code=204)
@app.get('/api/me')
def me(u=Depends(auth)):return {k:u[k] for k in ['id','email','studio','demo']}
@app.get('/api/capabilities')
def capabilities(u=Depends(auth)):return {'ai':ai.available(),'payment_processing':False,'offline_writes':False}
@app.post('/api/auth/demo')
def demo():
 if os.getenv('ALLOW_DEMO','1')!='1':raise HTTPException(403,'Demo workspaces disabled')
 with db.transaction() as c:
  u={'id':uid(),'email':uid()+'@demo.invalid','password':security.password_hash(secrets.token_urlsafe(32)),'studio':'The Thread Studio','demo':1};c.execute('INSERT INTO users VALUES(?,?,?,?,?,?)',(*u.values(),now()))
  samples=[('Ama Mensah','Occasion two-piece',-1,65000,30000,'Sewing'),('Kofi Asante','Linen kaftan',0,38000,38000,'Ready'),('Esi Owusu','Bridesmaid dress',2,52000,20000,'Cutting'),('Nana Boateng','Everyday shirt · 2 pieces',4,28000,10000,'Booked'),('Abena Cole','Evening dress',7,85000,40000,'Sewing')]
  for name,garment,days,total,paid,status in samples:
   oid=uid();due=(datetime.date.today()+datetime.timedelta(days=days)).isoformat();c.execute('INSERT INTO orders(id,owner,customer,garment,due,total,status,notes,created) VALUES(?,?,?,?,?,?,?,?,?)',(oid,u['id'],name,garment,due,total,status,'Fictional sample order',now()));event(c,u,oid,paid,'MoMo','Sample deposit');audit(c,u,oid,'Created','Fictional sample')
  return session(c,u)
@app.get('/api/orders')
def list_orders(u=Depends(auth)):
 with db.read() as c:return db.orders(c,u['id'])
@app.post('/api/orders',status_code=201)
def create(d:CreateOrder,u=Depends(auth),key:str=Header(alias='Idempotency-Key')):
 if d.deposit>d.total:raise HTTPException(422,'Deposit cannot exceed the order total')
 with db.transaction() as c:
  def work():
   oid=uid();c.execute('INSERT INTO orders(id,owner,customer,garment,due,total,status,notes,created) VALUES(?,?,?,?,?,?,?,?,?)',(oid,u['id'],d.customer,d.garment,d.due.isoformat(),d.total,'Booked',d.notes,now()))
   if d.deposit:event(c,u,oid,d.deposit,'Cash','Opening deposit recorded by owner')
   audit(c,u,oid,'Created','Order booked');return find(c,u,oid)
  return operation(c,u,key,{'action':'create',**d.model_dump(mode='json')},work)
@app.get('/api/orders/{oid}')
def detail(oid:str,u=Depends(auth)):
 with db.read() as c:
  out=find(c,u,oid);out['payments']=[dict(r) for r in c.execute('SELECT * FROM payments WHERE order_id=? AND owner=? ORDER BY created DESC',(oid,u['id']))];out['audit']=[dict(r) for r in c.execute('SELECT action,detail,created FROM audit WHERE order_id=? AND owner=? ORDER BY created DESC',(oid,u['id']))];return out
@app.put('/api/orders/{oid}')
def edit(oid:str,d:EditOrder,u=Depends(auth)):
 with db.transaction() as c:
  o=find(c,u,oid);mutable(o);version(o,d.version)
  if d.total<o['paid']:raise HTTPException(409,'Total cannot be less than payments already recorded. Record a refund first if appropriate.')
  c.execute('UPDATE orders SET customer=?,garment=?,due=?,total=?,notes=?,version=version+1 WHERE id=? AND owner=?',(d.customer,d.garment,d.due.isoformat(),d.total,d.notes,oid,u['id']));audit(c,u,oid,'Edited',f'Total {o["total"]} → {d.total}; due {o["due"]} → {d.due}');return find(c,u,oid)
TRANSITIONS={'Booked':['Cutting','Cancelled'],'Cutting':['Booked','Sewing','Cancelled'],'Sewing':['Cutting','Ready','Cancelled'],'Ready':['Sewing','Collected','Cancelled'],'Collected':[],'Cancelled':[]}
@app.post('/api/orders/{oid}/status')
def status(oid:str,d:ChangeStatus,u=Depends(auth)):
 with db.transaction() as c:
  o=find(c,u,oid);version(o,d.version)
  if d.status not in TRANSITIONS[o['status']]:raise HTTPException(409,'That status transition is not allowed')
  if d.status=='Collected' and o['paid']!=o['total']:raise HTTPException(409,'Record the remaining payment before collection')
  if d.status=='Cancelled' and o['paid']!=0:raise HTTPException(409,'Record any real refund before cancellation; net payments must be zero')
  c.execute('UPDATE orders SET status=?,version=version+1 WHERE id=? AND owner=?',(d.status,oid,u['id']));audit(c,u,oid,'Status',o['status']+' → '+d.status);return find(c,u,oid)
@app.post('/api/orders/{oid}/payments')
def payment(oid:str,d:Payment,u=Depends(auth),key:str=Header(alias='Idempotency-Key')):
 with db.transaction() as c:
  def work():
   o=find(c,u,oid);mutable(o);amount=d.amount if d.kind=='receipt' else -d.amount;new=o['paid']+amount
   if new<0 or new>o['total']:raise HTTPException(409,'Payment would exceed the balance, or refund would exceed recorded payments')
   event(c,u,oid,amount,d.method,d.note);c.execute('UPDATE orders SET version=version+1 WHERE id=? AND owner=?',(oid,u['id']));audit(c,u,oid,'Payment' if amount>0 else 'Refund',f'{amount} pesewas · {d.method}');return find(c,u,oid)
  return operation(c,u,key,{'action':'payment','id':oid,**d.model_dump()},work)
@app.get('/api/ledger')
def ledger(u=Depends(auth)):
 with db.read() as c:return [dict(r) for r in c.execute('SELECT p.*,o.customer,o.garment FROM payments p JOIN orders o ON o.id=p.order_id WHERE p.owner=? ORDER BY p.created DESC',(u['id'],))]
@app.get('/api/export')
def export(u=Depends(auth)):
 with db.read() as c:
  return {'exported_at':now(),'user':{k:u[k] for k in ['email','studio','demo']},'orders':db.orders(c,u['id']),'payments':[dict(r) for r in c.execute('SELECT * FROM payments WHERE owner=?',(u['id'],))],'audit':[dict(r) for r in c.execute('SELECT * FROM audit WHERE owner=?',(u['id'],))]}
@app.get('/api/export.csv')
def csv_export(u=Depends(auth)):
 with db.read() as c:rows=db.orders(c,u['id'])
 f=io.StringIO();w=csv.writer(f);w.writerow(['Customer','Garment','Due','Total GHS','Net paid GHS','Balance GHS','Status'])
 def safe(s):return "'"+s if s.lstrip().startswith(('=','+','-','@','\t','\r')) else s
 for o in rows:w.writerow([safe(o['customer']),safe(o['garment']),o['due'],f'{o["total"]/100:.2f}',f'{o["paid"]/100:.2f}',f'{(o["total"]-o["paid"])/100:.2f}',o['status']])
 return Response(f.getvalue(),media_type='text/csv',headers={'Content-Disposition':'attachment; filename="stitchledger-orders.csv"'})
@app.delete('/api/account')
def delete_account(d:DeleteAccount,u=Depends(auth)):
 if not u['demo'] and not security.verify(d.password,u['password']):raise HTTPException(401,'Password is incorrect')
 with db.transaction() as c:c.execute('DELETE FROM users WHERE id=?',(u['id'],))
 return {'deleted':True}
@app.post('/api/orders/{oid}/ai-draft')
def ai_draft(oid:str,d:Consent,u=Depends(auth)):
 if security.limited(('ai',u['id']),5,3600):raise HTTPException(429,'Hourly AI limit reached. Use the free template.')
 with db.read() as c:o=find(c,u,oid)
 return {'text':ai.draft(o['status'],o['due']),'source':'AI draft — review before sharing'}
# Relative web calls share this server. No wildcard CORS and no localhost in browser code.
WEB=Path(__file__).resolve().parents[1]/'web-build'
if WEB.exists():app.mount('/',StaticFiles(directory=WEB,html=True),name='web')
