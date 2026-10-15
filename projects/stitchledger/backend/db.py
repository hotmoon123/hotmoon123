"""SQLite repository boundary. Money is integer pesewas; writers serialize."""
import os,sqlite3
from pathlib import Path
from contextlib import contextmanager
DB=Path(os.getenv('STITCH_DB',str(Path(__file__).parent/'data'/'stitchledger.sqlite3')))
SCHEMA='''
CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY,email TEXT UNIQUE NOT NULL,password TEXT NOT NULL,studio TEXT NOT NULL,demo INTEGER NOT NULL DEFAULT 0,created TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sessions(token_hash TEXT PRIMARY KEY,user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,expires INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS orders(id TEXT PRIMARY KEY,owner TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,customer TEXT NOT NULL,garment TEXT NOT NULL,due TEXT NOT NULL,total INTEGER NOT NULL CHECK(total>=0),status TEXT NOT NULL CHECK(status IN ('Booked','Cutting','Sewing','Ready','Collected','Cancelled')),notes TEXT NOT NULL DEFAULT '',version INTEGER NOT NULL DEFAULT 1,created TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS orders_owner_due ON orders(owner,due);
CREATE TABLE IF NOT EXISTS payments(id TEXT PRIMARY KEY,owner TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,order_id TEXT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,amount INTEGER NOT NULL CHECK(amount!=0),method TEXT NOT NULL,note TEXT NOT NULL,created TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS payments_order ON payments(order_id);
CREATE TABLE IF NOT EXISTS audit(id TEXT PRIMARY KEY,owner TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,order_id TEXT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,action TEXT NOT NULL,detail TEXT NOT NULL,created TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS operations(owner TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,key TEXT NOT NULL,digest TEXT NOT NULL,result TEXT NOT NULL,PRIMARY KEY(owner,key));
PRAGMA user_version=1;
'''
def connection():
 DB.parent.mkdir(parents=True,exist_ok=True)
 c=sqlite3.connect(DB,timeout=15);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON');return c
def init():
 with connection() as c:
  c.execute('PRAGMA journal_mode=WAL');c.executescript(SCHEMA)
@contextmanager
def read():
 c=connection()
 try:yield c
 finally:c.close()
@contextmanager
def transaction():
 c=connection()
 try:
  c.execute('BEGIN IMMEDIATE');yield c;c.commit()
 except Exception:c.rollback();raise
 finally:c.close()
def order(c,owner,oid):
 return c.execute('SELECT o.*,COALESCE((SELECT SUM(amount) FROM payments WHERE order_id=o.id),0) paid FROM orders o WHERE o.id=? AND o.owner=?',(oid,owner)).fetchone()
def orders(c,owner):
 return [dict(r) for r in c.execute('SELECT o.*,COALESCE((SELECT SUM(amount) FROM payments WHERE order_id=o.id),0) paid FROM orders o WHERE o.owner=? ORDER BY due,created DESC',(owner,))]
