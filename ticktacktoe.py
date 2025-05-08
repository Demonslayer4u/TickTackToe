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

def get_board_con():
    return f"""   1   2   3
A  {board_raw[0]} | {board_raw[1]} | {board_raw[2]}
  ---+---+---
B  {board_raw[3]} | {board_raw[4]} | {board_raw[5]}
  ---+---+---
C  {board_raw[6]} | {board_raw[7]} | {board_raw[8]}
"""


#start
def start():
    print("TickTackToe")
    turnP1()


#menu
def menu():
    exityn = input("Play again (y/n)?")
    if exityn == "y":
        start()
    elif exityn == "n":
        exit()


#p1
def turnP1():
    print(" \nSpieler 1 (X) ist dran!")
    print(get_board_con())
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
    global SpalteInput
    global ZeileInput

    if SpalteInput == "1":
        if ZeileInput in ("A", "a"):
            board_raw[0] = "X"
            gewinnerkennungP1()
        elif ZeileInput in ("B", "b"):
            board_raw[3] = "X"
            gewinnerkennungP1()
        elif ZeileInput in ("C", "c"):
            board_raw[6] = "X"
            gewinnerkennungP1()
    elif SpalteInput == "2":
        if ZeileInput in ("A", "a"):
            board_raw[1] = "X"
            gewinnerkennungP1()
        elif ZeileInput in ("B", "b"):
            board_raw[4] = "X"
            gewinnerkennungP1()
        elif ZeileInput in ("C", "c"):
            board_raw[7] = "X"
            gewinnerkennungP1()
    elif SpalteInput == "3":
        if ZeileInput in ("A", "a"):
            board_raw[2] = "X"
            gewinnerkennungP1()
        elif ZeileInput in ("B", "b"):
            board_raw[5] = "X"
            gewinnerkennungP1()
        elif ZeileInput in ("C", "c"):
            board_raw[8] = "X"
            gewinnerkennungP1()
    else:
        print("Error 1")
        menu()

def gewinnerkennungP1():
    global board_raw
    if board_raw[0] == "X" and board_raw[1] == "X" and board_raw[2] == "X":
        winnerP1()
    elif board_raw[3] == "X" and board_raw[4] == "X" and board_raw[5] == "X":
        winnerP1()
    elif board_raw[6] == "X" and board_raw[7] == "X" and board_raw[8] == "X":
        winnerP1()
    elif board_raw[0] == "X" and board_raw[3] == "X" and board_raw[6] == "X":
        winnerP1()
    elif board_raw[1] == "X" and board_raw[4] == "X" and board_raw[7] == "X":
        winnerP1()
    elif board_raw[2] == "X" and board_raw[5] == "X" and board_raw[8] == "X":
        winnerP1()
    elif board_raw[0] == "X" and board_raw[4] == "X" and board_raw[8] == "X":
        winnerP1()
    elif board_raw[2] == "X" and board_raw[4] == "X" and board_raw[6] == "X":
        winnerP1()
    elif " " not in board_raw:
        print("Unentschieden!")
        print(get_board_con())
        menu()
    else: turnP2()

def winnerP1():
    print("Glückwunsch Spieler 1, du hast gewonnen!")
    print(get_board_con())
    menu()

#p2
def turnP2():
    print(" \nSpieler 2 (O) ist dran!")
    print(get_board_con())
    spaltenInputP2()

def spaltenInputP2():
    global SpalteInput
    SpalteInput = input("Wo setzt du deinen O? (Spalte)")
    if SpalteInput in ("1", "2", "3"):
        zeilenInputP2()
    else: spaltenInputP2()

def zeilenInputP2():
    global ZeileInput
    ZeileInput = input("Wo setzt du deinen O? (Zeile)")
    if ZeileInput in ("A", "B", "C", "a", "b", "c"):
        inputSetzenP2()
    else: zeilenInputP2()

def inputSetzenP2():
    global SpalteInput
    global ZeileInput

    if SpalteInput == "1":
        if ZeileInput in ("A", "a"):
            board_raw[0] = "O"
            gewinnerkennungP2()
        elif ZeileInput in ("B", "b"):
            board_raw[3] = "O"
            gewinnerkennungP2()
        elif ZeileInput in ("C", "c"):
            board_raw[6] = "O"
            gewinnerkennungP2()
    elif SpalteInput == "2":
        if ZeileInput in ("A", "a"):
            board_raw[1] = "O"
            gewinnerkennungP2()
        elif ZeileInput in ("B", "b"):
            board_raw[4] = "O"
            gewinnerkennungP2()
        elif ZeileInput in ("C", "c"):
            board_raw[7] = "O"
            gewinnerkennungP2()
    elif SpalteInput == "3":
        if ZeileInput in ("A", "a"):
            board_raw[2] = "O"
            gewinnerkennungP2()
        elif ZeileInput in ("B", "b"):
            board_raw[5] = "O"
            gewinnerkennungP2()
        elif ZeileInput in ("C", "c"):
            board_raw[8] = "O"
            gewinnerkennungP2()
    else:
        print("Error 2")
        menu()

def gewinnerkennungP2():
    global board_raw
    if board_raw[0] == "X" and board_raw[1] == "X" and board_raw[2] == "X":
        winnerP2()
    elif board_raw[3] == "X" and board_raw[4] == "X" and board_raw[5] == "X":
        winnerP2()
    elif board_raw[6] == "X" and board_raw[7] == "X" and board_raw[8] == "X":
        winnerP2()
    elif board_raw[0] == "X" and board_raw[3] == "X" and board_raw[6] == "X":
        winnerP2()
    elif board_raw[1] == "X" and board_raw[4] == "X" and board_raw[7] == "X":
        winnerP2()
    elif board_raw[2] == "X" and board_raw[5] == "X" and board_raw[8] == "X":
        winnerP2()
    elif board_raw[0] == "X" and board_raw[4] == "X" and board_raw[8] == "X":
        winnerP2()
    elif board_raw[2] == "X" and board_raw[4] == "X" and board_raw[6] == "X":
        winnerP2()
    else: turnP1()

def winnerP2():
    print("Glückwunsch Spieler 2, du hast gewonnen!")
    print(get_board_con())
    menu()


start()