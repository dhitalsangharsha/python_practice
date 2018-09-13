import sqlite3
con=sqlite3.connect('PQRS.db')
cur=con.cursor()

insert_sql_query = """
INSERT INTO product(name, price) values("BOOK", "500");
"""
cur.execute(insert_sql_query)
con.commit()

con.close()