from psycopg2 import connect
import random

CONNECTION = dict(dbname="testdb", user="testdbuser", password="TempP@$$", host="127.0.0.1", port="5432")

conn = connect(**CONNECTION)
cursor = conn.cursor()
cursor.execute("select 1;")
# print(cursor.fetchall())

# create table
# cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50), age INTEGER)")
# cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38), ('John', 28), ('Vova', 42), ('Maxim', 29), ('Petr', 35)")
# conn.commit()
# for person in cursor:
#     print(person)

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# print(cursor.fetchmany(2))
# print()
# print(cursor.fetchmany(2))
# print(cursor.fetchall())

# cursor.execute("select %s, %s from people;", ("name", "age"))
# print(cursor.fetchall())

# bob = ("Bob", 42)
# cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", bob)
# conn.commit()

# cursor.execute("select * from people;")
# print(cursor.fetchall())

# persons = [("vasia", 18), ("Linda", 99), ("Kolia", 55)]
# cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", persons)
# conn.commit()

class People:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return self.name
    
cursor.execute("select * from people;")
list_of_users = cursor.fetchall()

people_list = [People(*p) for p in list_of_users]
print(*people_list, sep="\n")