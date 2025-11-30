Our program resides in this root directory:
```
\sql-injection-lab\app
```
Access `\app\data` to initialize the database (.db) 

Create a `lab.db` file from `seed.sql` with `init_db.py`
```python
python data/init_db.py
```
Run the vulnerable website:
```python
PS C:\...\sql-injection-lab\app> python .\vuln_app.py 
 * Serving Flask app 'vuln_app'
 * Debug mode: off
```
The website is available on port `:5000` on our local machine

Access via: `127.0.0.1:5000`

<img width="565" height="362" alt="image" src="https://github.com/user-attachments/assets/f635e6d5-3026-45fd-aaa5-bb3421eb5eac" />

Two accessible routes or subpages in this app

`http://127.0.0.1:5000/login`
<img width="674" height="443" alt="image" src="https://github.com/user-attachments/assets/e936114f-b675-4bfe-b147-b00a9431e27a" />

`http://127.0.0.1:5000/search`
<img width="1231" height="500" alt="image" src="https://github.com/user-attachments/assets/87809967-0c19-424b-a3c0-a82da11f1cca" />

