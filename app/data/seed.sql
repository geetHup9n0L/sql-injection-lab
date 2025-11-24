BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT);
CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT);
INSERT INTO users (username, password) VALUES ('alice', 'alicepass');
INSERT INTO users (username, password) VALUES ('bob', 'bobpass');
INSERT INTO products (name, description) VALUES ('Apple', 'Fresh red apple');
INSERT INTO products (name, description) VALUES ('Banana', 'Yellow banana');
INSERT INTO products (name, description) VALUES ('Cherry', 'Small red cherry');
COMMIT;
