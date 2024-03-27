#http protokol i veb pregramiranje

'''import requests
#GET metoda
r = requests.get("https://xkcd.com/1906")
print(r)
print(r.status_code) '''

#primer1 konekcija na bazu
'''import mysql.connector as sql
mydb = sql.connect(user="root",host="localhost",password="gospodarsvega")
cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")
for i in cursor:
    print(i)
cursor.close()'''

#primer2 post zahtev + json
'''import requests
pload = {"username":"Olivia","password":"123"}
r = requests.post("https://httpbin.org/post",data=pload)
#print(r.text)
#print(r.json())
r_dict = r.json()
print(r_dict["form"])'''


