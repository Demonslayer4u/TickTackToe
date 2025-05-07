board_raw = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

board_con = f"""   1   2   3
A  {board_raw[0]} | {board_raw[1]} | {board_raw[2]}
  ---+---+---
B  {board_raw[3]} | {board_raw[4]} | {board_raw[5]}
  ---+---+---
C  {board_raw[6]} | {board_raw[7]} | {board_raw[8]}
"""

SpalteInput = None
ZeileInput = None



#start
def start():
    print("TickTackToe")
    turnP1()


#menu
def menu():
    exityn = input("Play again?")
    if exityn == "y":
        start()
    elif exityn == "n":
        exit()


#p1
def turnP1():
    print("Spieler 1 (X) ist dran!")
    print(board_con)
    spaltenInputP1()
def spaltenInputP1():
    global SpalteInput
    SpalteInput = input("Wo setzt du dein X? (Spalte)")
    if SpalteInput in ("1", "2", "3"):
        zeilenInputP1()
    else: spaltenInputP1()
def zeilenInputP1():
    global ZeileInput
    ZeileInput = input("Wo setzt du dein X? (Zeile)")
    if ZeileInput in ("A", "B", "C", "a", "b", "c"):
        inputSetzenP1()
    else: zeilenInputP1()
def inputSetzenP1():


#p2
def turnP2():
    print(board_con)





start()