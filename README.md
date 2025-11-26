# SQL Injection CTF Lab 

This repository provides a compact, intentionally vulnerable Flask app (login + search),
an exploit script that demonstrates UNION-based extraction against SQLite, and a patched
version using parameterized queries.

Quick start (local):
1. Create the DB:
   `cd /app`
   `python3 data/init_db.py`
2. Run the vulnerable app:
   `python3 vuln_app.py`
3. In another terminal run the exploit:
   `python3 ../exploit/exploit_sqli.py`

Or use Docker:
- `docker-compose up --build`

Notes:
- The vuln app logs executed SQL statements to app/logs/app.log (useful for the lab).
- Patched app demonstrates prepared statements; start it with `python patched_app.py`.

More detailed documents at: `/docs`
