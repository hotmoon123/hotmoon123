import hashlib,hmac,secrets,time
from collections import defaultdict,deque
from threading import Lock
ITERATIONS=600_000
BUCKETS=defaultdict(deque);LOCK=Lock()
def password_hash(password):
 salt=secrets.token_hex(16);value=hashlib.pbkdf2_hmac('sha256',password.encode(),bytes.fromhex(salt),ITERATIONS).hex();return f'{salt}${value}'
def verify(password,encoded):
 salt,want=encoded.split('$');actual=hashlib.pbkdf2_hmac('sha256',password.encode(),bytes.fromhex(salt),ITERATIONS).hex();return hmac.compare_digest(want,actual)
def digest(token):return hashlib.sha256(token.encode()).hexdigest()
def limited(key,limit,window=60):
 now=time.monotonic()
 with LOCK:
  q=BUCKETS[key]
  while q and q[0]<now-window:q.popleft()
  if len(q)>=limit:return True
  q.append(now)
  if len(BUCKETS)>10000:
   for k in list(BUCKETS):
    if not BUCKETS[k] or BUCKETS[k][-1]<now-window:BUCKETS.pop(k,None)
  return False
