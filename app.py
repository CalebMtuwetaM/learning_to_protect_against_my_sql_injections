# import the nessecary module
import sqlite3

# create the database table
conn = sqlite3.connect("people.db")

# setup the data in the database

cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS people;""")

cursor.execute("""CREATE TABLE people (
  name VARCHAR(255) NOT NULL,
  job VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  age INT,
  gender CHAR(1));""")

cursor.execute("""INSERT INTO people (name,job,password,age,gender) VALUES
('Mike','Programmer','mypass123','45','m'),
('Anna','Accountant','mysecret123','39','f'),
('Bob','Doctor','123456789','65','m'),
('Sam','Accountant','caleb5608','65','m');""")

conn.commit()

# a sort of a login interface where you input your name and your password and retrieve information about yourself

name_input = input("What is your name: ")
pass_input = input("What is your password: ")


cursor.execute(f"SELECT * FROM people WHERE name = '{name_input}' AND password = '{pass_input}'")

rows = cursor.fetchall()


if len(rows) == 0:
    print("Login Failed!")
else:
    print(f"Success! Here is the information of {name_input}")
    for row in rows:
        print(row)
