import sys, pathlib,uuid,concurrent.futures,time
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import pytest
from fastapi.testclient import TestClient
import db,security,main
@pytest.fixture
def client(tmp_path,monkeypatch):
 monkeypatch.setattr(db,'DB',tmp_path/'test.sqlite3');security.BUCKETS.clear()
 with TestClient(main.app) as c:yield c

def user(c,email='owner@example.com'):
 r=c.post('/api/auth/register',json={'email':email,'password':'aStrongExample12!','studio':'Test Studio'});assert r.status_code==201,r.text
 return {'Authorization':'Bearer '+r.json()['token']}
def key():return {'Idempotency-Key':uuid.uuid4().hex}
def order(c,h,**kw):
 d={'customer':'Demo Customer','garment':'Kaftan','due':'2026-11-01','total':10000,'deposit':2000};d.update(kw)
 r=c.post('/api/orders',headers=h|key(),json=d);assert r.status_code==201,r.text;return r.json()
def payment(c,h,o,amount,kind='receipt',k=None):return c.post(f'/api/orders/{o["id"]}/payments',headers=h|(k or key()),json={'amount':amount,'kind':kind,'method':'MoMo','note':'Recorded after confirmation'})
def change(c,h,o,state):return c.post('/api/orders/'+o['id']+'/status',headers=h,json={'status':state,'version':o['version']})

def test_auth_required(client):assert client.get('/api/orders').status_code==401

def test_register_login_logout(client):
 h=user(client);assert client.get('/api/me',headers=h).json()['studio']=='Test Studio'
 r=client.post('/api/auth/login',json={'email':'owner@example.com','password':'aStrongExample12!'});assert r.status_code==200
 assert client.post('/api/auth/logout',headers=h,json={}).status_code==204
 assert client.get('/api/me',headers=h).status_code==401

def test_wrong_password(client):
 user(client);r=client.post('/api/auth/login',json={'email':'owner@example.com','password':'nottherightpassword'});assert r.status_code==401

def test_password_and_email_validation(client):
 for email,password in [('bad','longPassword123'),('valid@example.com','short')]:assert client.post('/api/auth/register',json={'email':email,'password':password,'studio':'Test'}).status_code==422

def test_expired_session(client):
 h=user(client)
 with db.transaction() as c:c.execute('UPDATE sessions SET expires=0')
 assert client.get('/api/me',headers=h).status_code==401

def test_tenant_isolation(client):
 a=user(client);o=order(client,a);b=user(client,'other@example.com')
 assert client.get('/api/orders',headers=b).json()==[]
 assert client.get('/api/orders/'+o['id'],headers=b).status_code==404
 assert payment(client,b,o,100).status_code==404
 assert client.get('/api/ledger',headers=b).json()==[]
 assert client.get('/api/export',headers=b).json()['orders']==[]

def test_payment_idempotency(client):
 h=user(client);o=order(client,h);k=key()
 a=payment(client,h,o,1000,k=k);b=payment(client,h,o,1000,k=k)
 assert a.status_code==b.status_code==200
 assert a.json()['paid']==b.json()['paid']==3000
 assert len(client.get('/api/orders/'+o['id'],headers=h).json()['payments'])==2
 assert payment(client,h,o,2000,k=k).status_code==409

def test_create_idempotency(client):
 h=user(client);k=key();d={'customer':'Demo','garment':'Shirt','due':'2026-11-01','total':2000}
 a=client.post('/api/orders',headers=h|k,json=d);b=client.post('/api/orders',headers=h|k,json=d)
 assert a.json()['id']==b.json()['id'];assert len(client.get('/api/orders',headers=h).json())==1

def test_overpayment_and_refund(client):
 h=user(client);o=order(client,h)
 assert payment(client,h,o,8001).status_code==409
 assert payment(client,h,o,2001,'refund').status_code==409
 r=payment(client,h,o,1000,'refund');assert r.status_code==200;assert r.json()['paid']==1000

def test_integer_money(client):
 h=user(client)
 for n in [-1,0.1,'100',True,100000001]:
  assert client.post('/api/orders',headers=h|key(),json={'customer':'Test','garment':'Shirt','due':'2026-11-01','total':n}).status_code==422

def test_validation_and_extra_fields(client):
 h=user(client)
 for change_ in [{'due':'2026-02-31'},{'owner':'somebody'},{'customer':''},{'deposit':20000}]:
  d={'customer':'X','garment':'Y','due':'2026-11-01','total':1000}|change_
  assert client.post('/api/orders',headers=h|key(),json=d).status_code==422

def test_status_and_closed_order(client):
 h=user(client);o=order(client,h)
 assert change(client,h,o,'Collected').status_code==409
 for state in ['Cutting','Sewing','Ready']:o=change(client,h,o,state).json()
 assert change(client,h,o,'Collected').status_code==409
 o=payment(client,h,o,8000).json();o=change(client,h,o,'Collected').json()
 assert payment(client,h,o,100,'refund').status_code==409
 assert o['status']=='Collected'

def test_cancel_requires_refund(client):
 h=user(client);o=order(client,h)
 assert change(client,h,o,'Cancelled').status_code==409
 o=payment(client,h,o,2000,'refund').json();r=change(client,h,o,'Cancelled');assert r.status_code==200

def test_optimistic_version(client):
 h=user(client);o=order(client,h);assert change(client,h,o,'Cutting').status_code==200
 assert change(client,h,o,'Cutting').status_code==409

def test_edit_and_minimum_total(client):
 h=user(client);o=order(client,h);data={k:o[k] for k in ['customer','garment','due','total','notes','version']};data['total']=1000
 assert client.put('/api/orders/'+o['id'],headers=h,json=data).status_code==409
 data['total']=12000;assert client.put('/api/orders/'+o['id'],headers=h,json=data).status_code==200

def test_payment_rows_not_mutable_via_api(client):
 h=user(client);o=order(client,h);assert client.delete('/api/orders/'+o['id']+'/payments',headers=h).status_code in [405,404]

def test_concurrent_payment_guard(client):
 h=user(client);o=order(client,h,deposit=0,total=1000)
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(lambda _:payment(client,h,o,800).status_code,range(2)))
 assert sorted(results)==[200,409]
 assert client.get('/api/orders/'+o['id'],headers=h).json()['paid']==800

def test_account_deletion(client):
 h=user(client);order(client,h)
 assert client.request('DELETE','/api/account',headers=h,json={'confirmation':'DELETE','password':'incorrect-password'}).status_code==401
 assert client.request('DELETE','/api/account',headers=h,json={'confirmation':'DELETE','password':'aStrongExample12!'}).status_code==200
 assert client.get('/api/me',headers=h).status_code==401
 with db.read() as c:
  for table in ['users','sessions','orders','payments','audit','operations']:assert c.execute('SELECT COUNT(*) FROM '+table).fetchone()[0]==0

def test_csv_safety_and_json_export(client):
 h=user(client);order(client,h,customer='=1+1');r=client.get('/api/export.csv',headers=h)
 assert "'=1+1" in r.text
 export=client.get('/api/export',headers=h).json();assert 'password' not in export['user'];assert len(export['payments'])==1

def test_demo_isolation(client):
 a=client.post('/api/auth/demo').json();b=client.post('/api/auth/demo').json()
 ah={'Authorization':'Bearer '+a['token']};bh={'Authorization':'Bearer '+b['token']}
 ao=client.get('/api/orders',headers=ah).json();bo=client.get('/api/orders',headers=bh).json();assert len(ao)==len(bo)==5;assert ao[0]['id']!=bo[0]['id']

def test_ai_disabled_and_consent(client,monkeypatch):
 monkeypatch.delenv('OPENAI_API_KEY',raising=False);h=user(client);o=order(client,h)
 assert not client.get('/api/capabilities',headers=h).json()['ai']
 assert client.post('/api/orders/'+o['id']+'/ai-draft',headers=h,json={'consent':False}).status_code==422
 assert client.post('/api/orders/'+o['id']+'/ai-draft',headers=h,json={'consent':True}).status_code==503

def test_ai_minimal_context(client,monkeypatch):
 h=user(client);o=order(client,h);seen=[]
 monkeypatch.setattr(main.ai,'draft',lambda status,due:seen.append((status,due)) or 'Review this draft')
 r=client.post('/api/orders/'+o['id']+'/ai-draft',headers=h,json={'consent':True});assert r.status_code==200;assert seen==[('Booked','2026-11-01')]

def test_size_limit(client):assert client.post('/api/auth/login',content='x'*40000).status_code==413

def test_auth_rate_limit(client):
 for _ in range(20):client.post('/api/auth/login',json={})
 assert client.post('/api/auth/login',json={}).status_code==429

def test_security_headers(client):
 r=client.get('/api/health');assert r.headers['x-content-type-options']=='nosniff';assert r.headers['cache-control']=='no-store';assert 'x-request-id' in r.headers

def test_backup_restore(client,tmp_path):
 import backup
 h=user(client);order(client,h);dest=backup.backup(tmp_path/'copy.sqlite3')
 assert backup.verify_restore(dest)['orders']==1
 assert dest.stat().st_mode&0o777==0o600
 with pytest.raises(ValueError):backup.backup(dest)
