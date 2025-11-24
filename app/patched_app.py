# patched_app.py
# Same endpoints as vuln_app.py but using parameterized queries to prevent SQLi.
from flask import Flask, request, jsonify, render_template
import sqlite3, os, logging, re

app = Flask(__name__)
BASE = os.path.dirname(__file__)
DB = os.path.join(BASE, 'data', 'lab.db')
LOG = os.path.join(BASE, 'logs', 'app.log')
os.makedirs(os.path.join(BASE, 'logs'), exist_ok=True)

logging.basicConfig(filename=LOG, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

def query_db(sql, params=()):
    logging.info('SQL PARAM: %s -- %s', sql, params)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    # PATCHED: parameterized query prevents injection
    sql = 'SELECT id, username FROM users WHERE username=? AND password=?;'
    rows = query_db(sql, (username, password))
    if rows:
        return 'Welcome {}!'.format(rows[0][1])
    return 'Login failed', 401

@app.route('/search')
def search():
    q = request.args.get('q','')
    # Safe: use parameterized LIKE with bound parameter
    sql = 'SELECT id, name, description FROM products WHERE name LIKE ?;'
    like_q = f'%{q}%'
    rows = query_db(sql, (like_q,))
    results = [{'id': r[0], 'name': r[1], 'description': r[2]} for r in rows]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
