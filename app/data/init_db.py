# init_db.py -- creates lab.db from seed.sql if missing
import sqlite3, os
BASE = os.path.dirname(__file__)
DB = os.path.join(BASE, 'lab.db')
SQL = os.path.join(BASE, 'seed.sql')
if os.path.exists(DB):
    print('DB exists:', DB)
else:
    with open(SQL, 'r') as f:
        sql = f.read()
    conn = sqlite3.connect(DB)
    conn.executescript(sql)
    conn.close()
    print('Created DB at', DB)
