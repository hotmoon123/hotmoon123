"""Local backup and isolated restore verification; no background scheduling."""
import argparse,sqlite3,os,tempfile,json
from pathlib import Path
from datetime import datetime,timezone
import db

def backup(destination):
 destination=Path(destination)
 if destination.exists():raise ValueError('Destination exists; refusing to overwrite')
 if not db.DB.exists():raise ValueError('Source database does not exist')
 destination.parent.mkdir(parents=True,exist_ok=True)
 fd=os.open(destination,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.close(fd)
 try:
  with db.read() as source,sqlite3.connect(destination) as target:
   source.backup(target)
   if target.execute('PRAGMA integrity_check').fetchone()[0]!='ok':raise ValueError('Backup integrity failed')
 except Exception:destination.unlink(missing_ok=True);raise
 return destination

def verify_restore(source):
 with tempfile.TemporaryDirectory() as d:
  dest=Path(d)/'restore.sqlite3'
  with sqlite3.connect(f'file:{Path(source).resolve()}?mode=ro',uri=True) as src,sqlite3.connect(dest) as dst:
   src.backup(dst)
   assert dst.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
   assert not dst.execute('PRAGMA foreign_key_check').fetchall()
   return {t:dst.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in ['users','orders','payments','audit']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('action',choices=['backup','verify']);p.add_argument('path');a=p.parse_args()
 print(backup(a.path) if a.action=='backup' else json.dumps(verify_restore(a.path)))
