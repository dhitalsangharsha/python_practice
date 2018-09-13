import sqlite3

con=sqlite3.connect('PQRS.db')

cur=con.cursor()

data=cur.execute("SELECT * FROM product")

for each in data:
    print(each)