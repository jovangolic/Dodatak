#rad sa bazama podataka

#Zadatak 2.1. Konektovati se na bazu example.db pomoću sqlite3 modula. Napraviti tabelu City ako ne postoji\
#sa podacima: name(text), country(text,Primary key), number_od_citizens(int). Dodati 2 grada. Ispisati podatke iz baze.
'''import sqlite3 as sql
def connection():
    try:
        conn = sql.connect('temp.db')
        return conn
    except sql.Error as err:
        print(err)  
def sql_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS city(name TEXT, country TEXT PRIMARY KEY, num_of_citizen INT)")
    conn.commit()
    print('\ncity table is created') 
    grad1 = ('Beograd','Srbija',8000000)
    grad2 = ('Moskva','Rusija',150000000)
    grad3 = ('Jerusalim','Izrael',9000000) 
    cursor.executemany("INSERT INTO city VALUES(?,?,?)",(grad1,grad2,grad3))
    conn.commit()
    print('\ndata is entered')
    cursor.execute("SELECT * FROM city")
    data = cursor.fetchall()
    for i in data:
        print(i)
conn = connection()
sql_table(conn)
if conn:
    conn.close()
    print('\sqlite connection is closed')  '''

#Zadatak 2.2. Konektovati se na bazu example.db pomoću sqlite3 modula. Napraviti tabelu Faculty ako ne postoji\
#sa podacima:id (TEXT, PRIMARY KEY), country(TEXT), university (TEXT), name(TEXT). Dodati 3 fakulteta \
#I Ispisati podatke iz baze. Izbrisati podatak čija je vrednost polja name TMF. Ispisati opet podatke iz baze podataka. 
'''import sqlite3 as sql
conn = sql.connect('mydata.db')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS faculty(id TEXT PRIMARY KEY,country TEXT,university TEXT,name TEXT)")
#conn.commit()
data = [(1, 'Srbija', 'Univerzitet u Beogradu','ETF'),
(2, 'Srbija', 'Univerzitet u Novom Sadu','PMF'),
(3, 'Srbija', 'Univerzitet u Beogradu','TMF')]
#query = "INSERT INTO faculty VALUES(?,?,?,?)"
#cursor.executemany(query,data)
#conn.commit()
select = "SELECT * FROM faculty"
#cursor.execute(select)
#data = cursor.fetchall()
#for d in data: print(d)
query2 = "DELETE FROM faculty WHERE name = 'TMF'"
cursor.execute(query2)
conn.commit()
cursor.execute("SELECT * FROM faculty;")
data = cursor.fetchall()
for d in data: print(d)'''

#Zadatak 2.3. Konektovati se na bazu example.db pomoću sqlite3 modula. Napraviti tabelu Voce ako ne postoji sa podacima:\
#sifrra (TEXT, PRIMARY KEY), name(TEXT), price(FLOAT). Dodati 4 voća I Ispisati podatke iz baze.\
#Izbrisati podatak čija je vrednost polja name ’jabuka’ kao I podatak čija je cena 90.56 ako postoje.\
#Ispisati opet podatke iz baze podataka.
'''import sqlite3 as sql
conn = sql.connect('mydata.db')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS fruits(sifra TEXT PRIMARY KEY,name TEXT,price FLOAT)")
#conn.commit()
data = [(1, 'jabuka', 50.56),
(2, 'kruska', 80.6),
(3, 'banana', 90.56),
(4, 'ananas', 66.34)]
#cursor.executemany("INSERT INTO fruits VALUES(?,?,?)",data)
#conn.commit()
#cursor.execute("SELECT * FROM fruits")
#print(cursor.fetchall())
#cursor.execute("DELETE FROM fruits WHERE name='jabuka'")
#conn.commit()
#cursor.execute("SELECT * FROM fruits")
#print(cursor.fetchall())
cursor.execute("DELETE FROM fruits WHERE price=90.56")
conn.commit()
cursor.execute("SELECT * FROM fruits")
print(cursor.fetchall())'''

#Zadatak 2.4. Konektovati se na bazu example.db pomoću sqlite3 modula. Napraviti tabelu Persons ako ne postoji\
#sa podacima:personal_id (TEXT, PRIMARY KEY),  first_name(TEXT), last_name(TEXT), year_of_birth(INT).\
#Dodati 2 osobe, jednu parametriyovanim dodavanjem a drugu neparametrizovanim. Ispisati podatke iz baze.
'''import sqlite3 as sql
conn = sql.connect('mydata.db')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS persons(personal_id TEXT PRIMARY KEY,first_name TEXT,last_name TEXT,\
#    year_of_birth INT)")
#conn.commit()    
#neparametrizovano dodavanje
p1 = (23,'Laza', 'Lazic', 1995)
#cursor.execute("INSERT INTO persons VALUES(?,?,?,?)",p1)
#conn.commit()
#print('\nneparametrizovano dodavanje')
#cursor.execute("SELECT * FROM persons")
#print(cursor.fetchall())
#parametrizovano dodavanje
p2 = {"personal_id":12, 'first_name':'Mika', "last_name":'Mikic', "year_of_birth":1996}
cursor.execute("INSERT INTO persons VALUES(:personal_id,:first_name,:last_name,:year_of_birth)",p2)
conn.commit()
print('\nparametrizovano dodavanje')
cursor.execute("SELECT * FROM persons")
print(cursor.fetchall())'''

import flask;print(dir(flask))