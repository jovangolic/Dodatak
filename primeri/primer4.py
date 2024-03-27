#primer1 rad sa nitima
'''import threading
def worker(n):
    print("worker: %s" %n)
    return
threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()'''

#prime2 niti
'''import threading
import time
def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting') 
def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting') 
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name
w.start()
w2.start()
t.start()'''

#primer3 daemon niti
'''import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    ) 
def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()
d.join()
t.join()'''

#primer4 pravljenje sopstvene niti preko klase
'''import logging,threading
logging.basicConfig(level= logging.DEBUG,format="(%(threadName)-10s) %(message)s")
class MyThread(threading.Thread):
    def run(self):
        logging.debug('running')
        return
for i in range(5):
    t = MyThread()
    t.start()'''

#primer5 net programming server
'''import socket
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
sSocket.bind(("127.0.0.1",8005))
sSocket.listen()
print("Server is listening...")
sSocket.accept()
print("It was pleasure")
sSocket.close()'''

#primer6 soket server tcp
'''import socket
import time
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.bind(("localhost",8005))
sSocket.listen()
print("Listening for connection: ")
conn, addr = sSocket.accept() 
print("Connection received from ", addr)
data = conn.recv(1024)
print("Message from client: \n")
time.sleep(2)  
print(data)
conn.close()
sSocket.close()'''

#primer7 sinhronizacija server tcp
'''import socket
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sSocket.bind(("localhost",8005)) 
sSocket.listen()
conn, addr = sSocket.accept()
print(addr) 
conn.send(b"Hello and welcome")
print("Client said: ", conn.recv(256).decode("utf-8"))  
conn.send(b"Thank you")
sSocket.close()'''

#primer8 racunanje zbira server tcp
'''import socket
sServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sServer.bind(("localhost",8005))
sServer.listen()
client,addr = sServer.accept()
client.send(b"Enter number 1: ")
firstNumber = int(client.recv(32).decode("utf-8"))
client.send(b"Enter number 2: ")
secondNumber = int(client.recv(32).decode("utf-8"))
res = format(firstNumber + secondNumber)
client.send(bytes(res,"utf-8"))'''

#primer9 pogadjanje brojeva server tcp
'''import socket
import random
sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()
userSocket,addr = sSocket.accept()
playernumber    = int(userSocket.recv(128).decode("utf-8"))
compnumber      = random.randint(1,5)
if playernumber == compnumber:
    userSocket.send(b"Nice! I guessed that number")
else:
    userSocket.send(f"Wrong! I guessed {compnumber} and you typed {playernumber}".encode("utf-8"))
'''

#primer10 udp server
'''import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005))
msg = server.recvfrom(16)
print(msg)'''

#primer11 heartbeat server koristeci niti
'''import socket
import threading
import time
class Heartbeat(threading.Thread):
    def run(self):
        while True:
            time.sleep(5)
            server.sendto(f"{int(time.time())}".encode("utf-8"),clientaddr)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005)) 
data = server.recvfrom(128)
clientaddr = data[1] 
Heartbeat().start() 
while True:
    data = server.recvfrom(128)
    print(data[0].decode("utf-8"))'''

#primer12 udp server
'''import socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",8005))
msg = server.recvfrom(16)
print(msg)'''

#primer13 udp endpoint server
'''import socket 
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Pravljenje soketa za prenost datagrama IP v4
server.bind(("localhost",8005)) # povezivanje soketa sa ip adresom i portom
data = server.recvfrom(128) # server slusa (ceka poruku od klijenta) - vraca procitani objekat i ip-adresu soketa klijenta
print(data[0].decode("utf-8")) # stampanje poslatih podataka od strane klijenta
server.connect(data[1]) # konektovanje ka klijentu (data[1] je adresa klijenta)
server.send(b"Hello from me also") # slanje poruke klijentu
data = server.recvfrom(128) # prijem podataka od klijenta
print(data[0].decode("utf-8")) # ispis primljenih podataka (tek pošto su stigli podaci od klijenta)
server.send(b"Woow..we speak on the edge") # slanje poruke ka klijentu'''

#primer14 udp heartbeat server
'''import socket
import threading
import time
class Heartbeat(threading.Thread):
    def run(self):
        while True: # beskonacna petlja u kojoj se nit spava 5 sekundi pa salje podatke ka klijentu
            time.sleep(5)
            server.sendto(f"{int(time.time())}".encode("utf-8"),clientaddr)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # kreiranje soketa
server.bind(("localhost",8005)) # povezivanje soketa sa ip adresom i portom
data = server.recvfrom(128) # server slusa (ceka poruku od klijenta) - vraca procitani objekat i ip-adresu soketa klijenta
clientaddr = data[1] # konektovanje ka klijentu (data[1] je adresa klijenta)
Heartbeat().start() # pocetak rada niti 
while True: # neprekidno odluskivanje
    data = server.recvfrom(128) 
    print(data[0].decode("utf-8"))'''

#primer15 chat server
'''import socket
import selectors 
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #trenutno preuzimanje prethodnog soketa koji je koristio istu adresu
# i nezavisnost od protokola
ss.bind(("localhost",8005))
ss.listen()
ss.setblocking(False) # soket sada nije blokiran da mora da ceka odziv od konekretnog klijenta
users = {}
def broadcast(msg,sender = None):
    for sock in users: 
        if sender and sock == sender:
            continue
        sock.send(msg.encode("utf-8"))
def accept(sock):
    conn, addr = sock.accept() # kada se klijent konektuje server prihvata tu konekciju (accept())
	#kriticna sekcija
    conn.setblocking(True) # blokiranje neke druge konekcije
    username = conn.recv(1024).decode("utf-8")
    conn.setblocking(False) 
	#kraj kriticne sekcije
    users[conn] = username
    print(f"User {username} has entered room")
    broadcast(f"User {username} has entered room",conn)
    sel.register(conn, selectors.EVENT_READ, read) #registrovanje objekta conn za prijem (citanje) poruka 
def read(sock): 
    msg = sock.recv(1024).decode("utf-8")
    username = users[sock] 
    print(f"User {username} say {msg}") 
    broadcast(f"{username}: {msg}")
sel = selectors.DefaultSelector() # pravljenje selektora - namena mu je da prihvati visestruke konekcije
sel.register(ss,selectors.EVENT_READ,accept) #registrovanje objekta soketa (ss) za prihvatanje konekcije 
print("Chat server running...")
while True:
    events = sel.select() # ako je sel registrovan u metodi accept(), onda on vidi dogadjaj
    for key, mask in events: # key sadrzi objekat za kome je pridruzena radnja mask
        key.data(key.fileobj) # key.fileobj je socket objekat - data od toga je radnja koja treba da se uzvrsi (recimo read)
'''

#primer16 niti koristeci funkcije asinhronost
'''import _thread, time
def handler(i):  
    print(f"Hello from thread: {i}")
    print(f"Thread id: {i}")
for i in range(10):
    _thread.start_new_thread(handler,(i,))
time.sleep(1) # da ne zavrse pre glavne niti'''
#isti primer drugi nacin
'''import _thread, time
def handler(i):  
    #id = _thread.get_ident()
    print(f"Hello from thread: {i}")
    print(f"Thread id: {i}")
    #print(f"id je {id}")
for i in range(10):
    id = _thread.start_new_thread(handler,(i,))
    print(f"Created thread with id: {id}") 
time.sleep(1)'''

#primer17 callback funkcija
'''import threading,time
def cbf():
    id = threading.get_ident() 
    print(f"Hello from thread {id}")
t = threading.Thread(None,cbf) # ako ne pozovemo start() nista se ne desava
for i in range(10):
    t = threading.Thread(None,cbf)
    t.start()'''

#primer18 prekidanje niti
'''import threading, time
class MyThread(threading.Thread):
    active = False
    def stop_thread(self):
        self.active = False
    def run(self): 
            self.active = True
            print("I am going to sleep 10 seconds")
            for _ in range(10000): #u ovom slucaju moze i bez i
                time.sleep(0.001)
                if not self.active:
                    return
                print("Thread is running",threading.current_thread().ident)
mt = MyThread() 
mt2 = MyThread()
mt.start()  
mt2.start()
time.sleep(2)
print("Hey, wake up!")
mt.stop_thread()
mt2.stop_thread()'''

#primer19 trka puzeva koristeci niti
'''import threading, time, random
class Snail(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id
    def run(self):
        total_trip = 10
        while total_trip > 0:
            total_trip -= 1
            time.sleep(random.randint(1,5))   
            print(f"{total_trip}".rjust(self.id))
        print(f"Snail #{self.id} finished")
for i in range(50):
    Snail(i).start()'''

#primer20 kriticna sekcija
'''import threading,time
class MyThread(threading.Thread):
    def run(self):
        global zbir
        #obj.acquire()
        for i in range(10000000):
            obj.acquire()   #kriticna sekcija
            zbir += 1       #kriticna sekcija    
            obj.release()   #kriticna sekcija
        #obj.release()    
        print("thread is running",zbir)    
zbir = 0   
obj = threading.Condition()     
mt = MyThread()
mt2 = MyThread()
mt3 = MyThread()
mt.start()
mt2.start()
mt3.start()
mt.join()
mt2.join()
mt3.join()
print("zbir je: ",zbir)'''

#primer21 niti
'''import threading,random
class MyThread(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id
    def run(self):
        print("Thread is running")
niti = []
suma = 0
for i in range(6): #kreiranje niti sa slucajnom vrednoscu
    niti.append(MyThread(random.randint(1,10)))
for i in range(6): #pokretanje niti
    niti[i].start() 
for i in range(6): #sabiranje vrednosti niti
    suma += niti[i].id
for i in range(6): #cekanje da sve nii zavrse
    niti[i].join()
print(suma)  '''


#primer22 pohlepni algoritam iterativno
'''class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu
def greedy(items, maxCost, keyFunction): #keyFunction je za sortiranje
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of Items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
#voce = ["jabuka","kruska","dinja","sljiva"]
#val = [25,30,29,34]
#cal = [300,350,289,320]
#total = buildMenu(voce,val,cal)
#print(total)'''

#primer23 ranac iterativno pohlepni algoritam
'''kalorije = [8,7,16,6,5,4]
maxKaloricnost = 20
kalorije = sorted(kalorije,reverse=True)
total = []
zbir = 0
for i in range(len(kalorije)):
    if(kalorije[i]+zbir<=maxKaloricnost): 
        total.append(kalorije[i])
        zbir += kalorije[i]
print(total)
print(zbir)  '''

#primer24 zero/one knapsack problem rekurzivno
'''class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu
def greedy(items, maxCost, keyFunction):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of Items to numbers"""
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)
def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)
def maxVal(toConsider, avail): #koristi rekurziju
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
        print(result[0],end=",")
    return result 
def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)
print('')
testMaxVal(foods, 750)'''


#primer25 greedy method ima-nema rekurzija
'''def rek(n):
    if(n==broj):
        suma=0
        global maxi
        print(a)
        for i in range(broj):
            if(a[i]==1):
                suma+=stavke[i]
        print(suma)
        if(suma>maxi and suma<=kapacitet):
            maxi = suma
    else:
        a[n]=0
        rek(n+1)
        a[n]=1
        rek(n+1)
stavke = [5,7,9]
a = [0,0,0]
kapacitet=16
broj = len(stavke)  # = 3
maxi = 0
rek(0)
print(maxi)  '''




