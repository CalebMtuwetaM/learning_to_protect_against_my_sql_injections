import sqlite3

conn = sqlite3.connect("people.db")

cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS people;""")

cursor.execute("""CREATE TABLE people (
  name VARCHAR(255) NOT NULL,
  job VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  age INT,
  gender CHAR(1))""")

cursor.execute("""INSERT INTO people (name,job,password,age,gender) VALUES
('Mike','Programmer','mypass123','45','m'),
('Anna','Accountant','mysecret123','39','f'),
('Bob','Doctor','123456789','65','m'),
('Sam','Accountant','caleb5608','65','m');""")

conn.commit()
