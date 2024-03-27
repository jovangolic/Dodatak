#iks oks prvi nacin/ ne radi
'''print("iks-oks igrica")
kraj = True
polja = [["P","P","P"],["P","P","P"],["P","P","P"]]
def tabla(polje):
    for i in range(len(polja)):
        for j in range(len(polja)):
            print(polje[i][j],end=" ")
        print() 
def is_kraj():
    for i in range(len(polja)):
        for j in range(len(polja)):
            if((polja[0][0]=="X")and(polja[0][1]=="X")and(polja[0][2]=="X")
               or(polja[1][0]=="X")and(polja[1][1]=="X")and(polja[1][2]=="X")or
               (polja[2][0]=="X")and(polja[2][1]=="X")and(polja[2][2]=="X") or
               (polja[0][0]=="X")and(polja[1][0]=="X")and(polja[2][0]=="X") or
               (polja[0][1]=="X")and(polja[1][1]=="X")and(polja[2][1]=="X") or
               (polja[0][2]=="X")and(polja[1][2]=="X")and(polja[2][2]=="X") or
               ((polja[i][j]=="X")and i==j) or((polja[i][j]=="X") and (i+j)==(2))):
                print("igrac1 (x) je pobedio") 
                return False
            elif ((polja[0][0]=="Y")and(polja[0][1]=="Y")and(polja[0][2]=="Y")
               or(polja[1][0]=="Y")and(polja[1][1]=="Y")and(polja[1][2]=="Y")or
               (polja[2][0]=="Y")and(polja[2][1]=="Y")and(polja[2][2]=="Y") or
               (polja[0][0]=="Y")and(polja[1][0]=="Y")and(polja[2][0]=="Y") or
               (polja[0][1]=="Y")and(polja[1][1]=="Y")and(polja[2][1]=="Y") or
               (polja[0][2]=="Y")and(polja[1][2]=="Y")and(polja[2][2]=="Y") or
               ((polja[i][j]=="Y")and i==j) or((polja[i][j]=="Y") and (i+j)==(2))):
                print("igrac2 (y) je pobedio") 
                return False   
            else:
                return True      
def igrac1():
    red = int(input("unesi X=x: "))
    kolona = int(input("unesi X=y: "))
    polja[red][kolona] = "X "
    tabla(polja)
    is_kraj()
def igrac2():
    red = int(input("unesi X=x: "))
    kolona = int(input("unesi X=y: "))
    polja[red][kolona] = "Y "
    tabla(polja)
    is_kraj()
while kraj:
    igrac1()
    igrac2()     '''

#iks-oks drugi nacin
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
print("Kratak opis: Igra je za dva igraca, Igrac br. 1 je X, i, Igrac br.2 je O")    
print("Napomena: Polja na IKS-OKS tabeli su numerisana kao na desnoj strani tastature koja je odredjena za racunske operacije.")
print("Polozaj broja na tastaturi odgovara polozaju vaseg odigranog poteza na dijagramu igre.")
board_keys = []
for key in theBoard:
    board_keys.append(key) 
#print(board_keys)               
def print_board(board):
    print(board["7"] + '|' + board["8"] + '|' + board["9"])
    print("-+-+-")
    print(board["4"] + '|' + board["5"] + '|' + board["6"])
    print("-+-+-")
    print(board["1"] + '|' + board["2"] + '|' + board["3"])
#print_board(theBoard)
def game():
    turn = "X"
    count = 0
    for i in range(10):
        print_board(theBoard)
        print("Sada si ti na potezu," + turn + ".Koje polje zelis da izaberes?")
        move = input()
        if theBoard[move] == " ":
            theBoard[move] = turn
            count += 1
        else:
            print("Polje koje ste izabrali je zauzeto.\nIzaberite drugo polje!")
            continue
        if count >= 5:
            if theBoard["7"] == theBoard["8"] == theBoard["9"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["4"] == theBoard["5"] == theBoard["6"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["1"] == theBoard["2"] == theBoard["3"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["1"] == theBoard["4"] == theBoard["7"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["2"] == theBoard["5"] == theBoard["8"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["3"] == theBoard["6"] == theBoard["9"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["7"] == theBoard["5"] == theBoard["3"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break
            elif theBoard["9"] == theBoard["5"] == theBoard["1"] != " ":
                print_board(theBoard)
                print("\Kraj igre.\n")
                print(" **** "+turn + " je pobedio. **** ")
                break 
        if count == 9:
            print("\nKraj igre.\n")
            print("IGRA JE NERESENA!!!!")
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    restart = input("Da li zelite da pocnete novu igru? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "
        game()
    else:
        exit()    
if __name__ == "__main__":
    game()                                                   
                 