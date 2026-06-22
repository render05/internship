import sqlite3
import os

conn = sqlite3.connect("db1.db")

# sql = """
# CREATE TABLE emp(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(50),
# mob VARCHAR(43),
# city VARCHAR(43)
# )
# """
# sql = '''insert into emp(name,mob,city) values("abc",1234567,"jaipur")'''
# sql = '''select * from emp'''
# res = conn.execute(sql)
# for row in res:
#     print(row)
# sql = '''delete *from emp'''
# res = conn.execute(sql)
# for row in res:
#      print(row)
#      sql = delete * from emp where id =1
sql = '''select* from emp order by name desc'''
res = conn.execute(sql)
for row in res:
print(row)
#      sql = delete * from emp where id =

conn.execute(sql)
conn.commit()
conn.close()

