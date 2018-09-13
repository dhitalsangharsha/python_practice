import sqlite3

#connect to database
con=sqlite3.connect('PQRS.db')

#generate cursor

cur=con.cursor()

#define a SQL query string
create_table_query='''CREATE TABLE product(
                    name text NOT NULL,
                    price text NOT NULL)
                    '''
#execute the query
cur.execute(create_table_query)