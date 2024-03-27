'''from primer2 import Tacka as t
a = t(1,0)
b = t(0,1)
c = t()
d = a + b
d2 = a - b
print(d)  
print(d2)
print(a == b)
print(a+b)
print(a - b)'''

'''from primer2 import Osoba as f
z = f('Aca', 'Vukic', '12153', 95000, '3a', '4218-589')
s = f('Mitar', 'Miric', '12131', '119/17', 'MTI')
print(isinstance(s, f), isinstance(s, f))
z.predstavi_se()
s.predstavi_se()
print(z)'''

#primer5 net programming klijent
'''import socket
sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("127.0.0.1",8005))
sClient.close()'''

#primer6 soket klijent tcp
'''import socket 
cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect(("localhost",8005))
cSocket.send(b"Hey man, what's up?") 
cSocket.sendall(b"Are you there?") 
cSocket.close()'''

#primer7 sinhronizacija klijent tcp
'''import socket
sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("localhost",8005))
print("Server said: ", sClient.recv(256).decode("utf-8"))
msg = input("msg: ")
sClient.send(bytes(msg,"utf-8"))
print("Server said: ", sClient.recv(256).decode("utf-8"))
sClient.close()'''

#primer8 racunanje zbira klijent tcp
'''import socket
cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect(("localhost",8005))
firstNum = input(cSocket.recv(256).decode("utf-8"))
cSocket.send(bytes(firstNum,"utf-8"))
secondNum = input(cSocket.recv(256).decode("utf-8"))
cSocket.send(bytes(secondNum,"utf-8"))
print("Result is: ", cSocket.recv(256).decode("utf-8"))'''

#primer9 pogadjanje brojeva klijent tcp
'''import socket
playerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
playerSocket.connect(("localhost",8005))
playerSocket.send(bytes(input("Enter number: "),"utf-8"))
print(playerSocket.recv(128).decode("utf-8"))'''

#primer10 udp klijent
'''import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("localhost",8005))
client.send(b"Hello world")'''

#primer11 heartbeat klijent koristeci niti
'''import socket
import threading
import time
class Heartbeat(threading.Thread):
    def run(self):
        global client
        while True:
            print("Heartbeat " , client.recv(128).decode("utf-8"))
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("localhost",8005)) 
client.send(b"Hello") 
Heartbeat().start()
day = 0
while True:
    client.send(f"Hello, groundhog day {day}".encode("utf-8")) 
    time.sleep(10)'''
         
#primer12 udp klijent
'''import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("localhost",8005))
client.send(b"Hello world")     '''

#primer13 udp endpoint klijent
'''import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Pravljenje soketa
client.connect(("localhost",8005))
#client.sendto(b"Hello")
client.send(b"Hello")
print(client.recv(128).decode("utf-8"))
client.send(b"Hello again")
print(client.recv(128).decode("utf-8"))'''

#primer14 udp heartbeat klijent
'''import socket
import threading
import time
class Heartbeat(threading.Thread):
    def run(self):
        global client
        while True: # beskonacna petlja u kokoj se nit spa 5 sekundi pa salje podatke ka klijentu
            print("Heartbeat " , client.recv(128).decode("utf-8"))
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # kreiranje soketa
client.connect(("localhost",8005)) #konekcija ka serveru
client.send(b"Hello") # slanje poruke serveru
Heartbeat().start() # pocetak rada niti
day = 0
while True: # neprekidno odluskivanje
    client.send(f"Hello, groundhog day {day}".encode("utf-8")) 
    day += 1
    time.sleep(10)'''


#primer15 chat klijent
'''import socket
import threading 
import sys
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
class ChatListener(threading.Thread):
    username = ""
    def __init__(self, username):
        super().__init__() # nasledjuje klasu threading.Thread, zato se koristi super()
        self.username = username
    def run(self): 
        client.connect(("127.0.0.1",8005))
        client.send(self.username.encode("utf-8"))
        while True:
            res = client.recv(1024).decode("utf-8")
            if res != "":
                print(res)     
username = input("Enter username: ")    
chat = ChatListener(username)
chat.daemon = True
chat.start()
while True:
    print("Enter message: ")
    msg = input()  
    client.send(msg.encode("utf-8"))'''


