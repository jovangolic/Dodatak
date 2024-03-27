#python sqlite database exercises at w3resource.com
#Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database
'''import sqlite3 as sql
try:
    conn = sql.connect('temp.db')
    cursor = conn.cursor()
    print('\ndatabase created and connected to SQLite')
    query_select = "select sqlite_version()"
    cursor.execute(query_select)
    record = cursor.fetchall()
    print('SQLite database version is: ',record)
    conn.close()
except sql.Error as error:
    print('\nerror while connecting to sqlite',error)
    conn.rollback()
finally:
    if conn:
        conn.close()
        print('\nsqlite connection is closed')'''

#Write a Python program to create a SQLite database connection to a database that resides in the memory.
'''import sqlite3 as sql
try:
    connection = sql.connect('temp.db')
    conn = sql.connect(":memory:")
    cursor = conn.cursor()
    print('\nmemory database created and connected to sqlite')
    select = "select sqlite_version();"
    cursor.execute(select)
    data = cursor.fetchall()
    print('\nsqlite database version is ',data)
    conn.close()
except sql.Error as error:
    print('\nerror while connection to sqlite',error)
    conn.rollback()
finally:
    if conn:
        conn.close()
        print('\nsqlite connection is closed') '''

#Write a Python program to connect a database and create a SQLite table within the database.
'''import sqlite3 as sql
def sql_connection():
    try:
        conn = sql.connect('temp.db')
        return conn
    except sql.Error as error:
        print(error)
def sql_table(conn):
    cursor = conn.cursor()
    select = ("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),\
        commission decimal(10,2),phone_no char(15) NULL);")
    cursor.execute(select)
    print('\nagent_master file has created')
    conn.commit()
conn = sql_connection()
sql_table(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed')   '''

#Write a Python program to list the tables of given SQLite database file
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('database.db')
        return conn
    except sql.Error as err:
        print(err)
def sql_table(conn):
    cursor = conn.cursor()        
    cursor.execute("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")
    cursor.execute("CREATE TABLE temp_agent_master(agent_code char(6),agent_name char(40),working_area char(35),commission decimal(10,2),phone_no char(15) NULL);")  
    print('list of tables')               
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    conn.commit()
conn = connection()
sql_table(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed') '''

#Write a Python program to create a table and insert some records in that table.\
#Finally selects all rows from the table and display the records   
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('example.db')
        return conn
    except sql.Error as err:
        print(err)
def sql_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
    cursor.executescript("INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);\
        INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);\
        INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);\
        INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);\
        INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);")            
    conn.commit()
    cursor.execute("SELECT * FROM salesman")
    print('agent details:')
    records = cursor.fetchall()
    for row in records:
        print(row)
conn = connection()
sql_table(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed') '''

#Write a Python program to insert a list of records into a given SQLite table
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('example.db')
        return conn
    except sql.Error as err:
        print(err)
def table(conn,rows):
    cursor = conn.cursor()   
    cursor.execute("CREATE TABLE salesman2(salesman_id n(5),name char(30),city char(35),\
        commission decimal(7,2));")         
    insert_query = """INSERT INTO salesman2(salesman_id,name,city,commission) VALUES(?,?,?,?);"""
    cursor.executemany(insert_query,rows)
    conn.commit()
    print('number of records after inserting rows')
    cur = cursor.execute("SELECT * FROM salesman2")
    print(len(cur.fetchall()))
rows = [(5001,'James Hoog', 'New York', 0.15),
                (5002,'Nail Knite', 'Paris', 0.25),
                (5003,'Pit Alex', 'London', 0.15),
                (5004,'Mc Lyon', 'Paris', 0.35),
                (5005,'Paul Adam', 'Rome', 0.45)]        
conn = connection()
table(conn,rows)
if conn:
    conn.close()
    print('\nsqlite connection is closed')   '''

#Write a Python program to insert values to a table from user input.
'''import sqlite3 as sql
conn = sql.connect('example.db')
cursor = conn.cursor()     
#create_query = "CREATE TABLE sales(salesman_id n(5),name char(30),city char(35),commission decimal(7,2));"
#cursor.execute(create_query)
#conn.commit()                        
s_id = int(input('salesman_id: '))
name = input('name: ')
city = input('city: ')
commission = input('commission: ')
insert = "INSERT INTO sales(salesman_id,name,city,commission) VALUES(?,?,?,?)"
cursor.execute(insert,(s_id,name,city,commission))
conn.commit()  
print('data entered successfully')
conn.close()
if conn:
    conn.close()
    print('\nsqlite connection is closed') '''

#Write a Python program to count the number of rows of a given SQLite table.
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('mydata.db')
        return conn
    except sql.Error as err:
        print(err)
def count_rows(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE sales(salesman_id n(5),name char(30),city char(35),commission decimal(7,2));")
    conn.commit()
    cur = cursor.execute("SELECT * FROM sales")
    print('number of records before inserting rows: ')
    print(len(cur.fetchall()))
    cursor.executescript("""INSERT INTO sales VALUES(5001,'James Hoog', 'New York', 0.15);\
    INSERT INTO sales VALUES(5002,'Nail Knite', 'Paris', 0.25);\
    INSERT INTO sales VALUES(5003,'Pit Alex', 'London', 0.15);\
    INSERT INTO sales VALUES(5004,'Mc Lyon', 'Paris', 0.35);\
    INSERT INTO sales VALUES(5005,'Paul Adam', 'Rome', 0.45);""")
    conn.commit()
    cur2 = cursor.execute("SELECT * FROM sales") 
    print('number of records after inserting rows: ')
    print(len(cur2.fetchall()))     
conn = connection()
count_rows(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed')  '''

#Write a Python program to update a specific column value of a given table and select all rows before\
#and after updating the said table.             
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('mydata.db')
        return conn
    except sql.Error as err:
        print(err)
def sql_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vendor(salesman_id n(5),name char(30),city char(35),commission decimal(7,2));")
    cursor.executescript("INSERT INTO vendor VALUES(5001,'James Hoog','New York',0.15);\
                        INSERT INTO vendor VALUES(5002,'Nail Knite','Paris',0.25);\
                        INSERT INTO vendor VALUES(5003,'Pit Alex','London',0.15);\
                        INSERT INTO vendor VALUES(5004,'Mc Lyon','Paris',0.35);\
                        INSERT INTO vendor VALUES(5005,'Paul Adam','Rome',0.45);")
    conn.commit()
    print('agent details')            
    cursor.execute("SELECT * FROM vendor")
    data = cursor.fetchall()
    for d in data:
        print(d)
    print('\nupdate commission .15 to .45 where id is 5003:')
    cursor.execute("UPDATE vendor SET commission = .45 WHERE salesman_id == 5003")
    conn.commit()
    print('\nrecord updated successfully')
    cursor.execute("SELECT * FROM vendor")
    print('\nafter updating agent details:')
    data = cursor.fetchall()
    for d in data:
        print(d)
conn = connection()
sql_table(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed') '''

#Write a Python program to update all the values of a specific column of a given SQLite table
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('example.db')
        return conn
    except sql.Error as err:
        print(err)
def updated_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vendor2(salesman_id n(5),name char(30),city char(35),commission decimal(7,2));")                      
    cursor.executescript("INSERT INTO vendor2 VALUES(5001,'James Hoog','New York',0.15);\
                    INSERT INTO vendor2 VALUES(5002,'Nail Knite','Paris',0.25);\
                    INSERT INTO vendor2 VALUES(5003,'Pit Alex','London',0.15);\
                    INSERT INTO vendor2 VALUES(5004,'Mc Lyon','Paris',0.35);\
                    INSERT INTO vendor2 VALUES(5005,'Paul Adam','Rome',0.45);")
    conn.commit()
    cursor.execute("SELECT * FROM vendor2")
    print('\nagent details')
    data = cursor.fetchall()
    for d in data:
        print(d)     
    print('\nupdate all commission to .55:')
    cursor.execute("UPDATE vendor2 SET commission = .55")
    conn.commit()
    print('\nrecord successfully updated')
    cursor.execute("SELECT * FROM vendor2")
    print('\nafter updating agent details')
    data = cursor.fetchall()
    for d in data:
        print(d)
conn = connection()
updated_table(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed.') '''

#Write a Python program to delete a specific row from a given SQLite table
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('example.db')
        return conn
    except sql.Error as err:
        print(err)
def delete_row(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vendor3(salesman_id n(5),name char(30),city char(35),commission decimal(7,2));")                      
    cursor.executescript("INSERT INTO vendor3 VALUES(5001,'James Hoog','New York',0.15);\
                    INSERT INTO vendor3 VALUES(5002,'Nail Knite','Paris',0.25);\
                    INSERT INTO vendor3 VALUES(5003,'Pit Alex','London',0.15);\
                    INSERT INTO vendor3 VALUES(5004,'Mc Lyon','Paris',0.35);\
                    INSERT INTO vendor3 VALUES(5005,'Paul Adam','Rome',0.45);")
    conn.commit()
    cursor.execute("SELECT * FROM vendor2")
    print('\nagent details')
    data = cursor.fetchall()
    for d in data:
        print(d) 
    print('\ndelete salesman of ID 5003: ')
    cursor.execute("DELETE FROM vendor3 WHERE salesman_id == 5003")
    conn.commit()
    cursor.execute("SELECT * FROM vendor3")
    print('\nafter deleting agent details')
    data = cursor.fetchall()
    for d in data:
        print(d)
conn = connection()
delete_row(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed')'''

#Write a Python program to alter a given SQLite table.
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('mydata.db')
        return conn
    except sql.Error as err:
        print(err)
def alter_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE agent_master(agent_code char(6),agent_name char(40),working_area char(35),\
        commission decimal(10,2),phone_no char(15) Null);")  
    print('\nagent file has created')
    print('\ntable structure of agent')
    c = conn.execute("PRAGMA table_info('agent_master')")
    for i in c:
        print(i)
    cursor.execute("ALTER TABLE agent_master ADD COLUMN FLAG BOOLEAN")
    print('\nagent file is altered')
    c = conn.execute("PRAGMA table_info('agent_master')")
    print('\ntable structure of agent')
    for i in c:
        print(i)
    conn.commit()    
conn = connection()
alter_table(conn)
if conn:
    conn.close()
    print('\nsqlite connection is closed')  '''

#Write a Python program to create a backup of a SQLite database                                        
'''import sqlite3 as sql
import io
conn = sql.connect('mydata.db')
with io.open('backup_data.sql','w') as f:
    for line in conn.iterdump():
        f.write('%s\n'%line)
print('backup performed successfully')
print('saved as mydatabase_dump.sql') 
conn.close()    '''

              

        
