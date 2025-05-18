board_raw = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

board_con = f"""   1   2   3
A  {board_raw[0]} | {board_raw[1]} | {board_raw[2]}
  ---+---+---
B  {board_raw[3]} | {board_raw[4]} | {board_raw[5]}
  ---+---+---
C  {board_raw[6]} | {board_raw[7]} | {board_raw[8]}
"""

split_input = None
line_input = None

input0 = None
input1 = None

input0_is_int = False
input1_is_int = False

player_turn = "X"


def get_board_con():
    #print("Board updated...")
    return f"""   1   2   3
A  {board_raw[0]} | {board_raw[1]} | {board_raw[2]}
  ---+---+---
B  {board_raw[3]} | {board_raw[4]} | {board_raw[5]}
  ---+---+---
C  {board_raw[6]} | {board_raw[7]} | {board_raw[8]}
"""

#reset
def reset_board():
    board_raw[0] = " "
    board_raw[1] = " "
    board_raw[2] = " "
    board_raw[3] = " "
    board_raw[4] = " "
    board_raw[5] = " "
    board_raw[6] = " "
    board_raw[7] = " "
    board_raw[8] = " "
    #print("Board reset..")
    user_input()


#start
def start():
    global player_turn
    reset_board()
    player_turn = "X"
    print("TickTackToe")
    #print("Start...")



#menu
def menu():
    #print("menu...")
    exityn = input("Play again (y/n)?")
    if exityn == "y":
        start()
    elif exityn == "n":
        exit()



#input
def user_input():
    #print("User_input...")

    global player_turn
    print(f" \nSpieler {player_turn} ist dran!")
    print(get_board_con())

    global input0
    global input1
    input_raw = input(f"Setze dein {player_turn} \n")
    input_raw = input_raw[:2]
    input0 = input_raw[0]
    input1 = input_raw[1]
    conversion1()



def conversion1():
    global input0
    global input0_is_int
    #print("Conversion1...")
    try:
        input0 = int(input0)
        input0_is_int = True
        conversion2()
    except ValueError:
        input0 = str(input0)
        input0_is_int = False
        conversion2()

def conversion2():
    global input1
    global input1_is_int
    #print("Conversion2...")
    try:
        input1 = int(input1)
        input1_is_int = True
        checking_input()
    except ValueError:
        input1 = str(input1)
        input1_is_int = False
        checking_input()

def checking_input():
    global input0_is_int
    global input0_is_int
    global split_input
    global line_input
    #print("Checking_input...")
    #print(Player_turn)

    if input0_is_int == input1_is_int:
        print("Ungültige Eingabe")
        user_input()
    else:
        if input0_is_int:
            split_input = str(input0)
            line_input = str(input1)
            #print("Inp0 is int...")
            placing()
        elif input1_is_int:
            #print("Inp1 is int...")
            split_input = str(input1)
            line_input = str(input0)
            placing()
        else:
            print("Error: Überprüfung")
            menu()



#input placen
def placing():
    global split_input
    global line_input
    #print("split: ",split_input)
    #print("line: ",line_input)

    if split_input == "1":
        if line_input in ("A", "a"):
            if board_raw[0] == " ":
                board_raw[0] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
        elif line_input in ("B", "b"):
            if board_raw[3] == " ":
                board_raw[3] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
        elif line_input in ("C", "c"):
            if board_raw[6] == " ":
                board_raw[6] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
    elif split_input == "2":
        if line_input in ("A", "a"):
            if board_raw[1] == " ":
                board_raw[1] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
        elif line_input in ("B", "b"):
            if board_raw[4] == " ":
                board_raw[4] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
        elif line_input in ("C", "c"):
            if board_raw[7] == " ":
                board_raw[7] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
    elif split_input == "3":
        if line_input in ("A", "a"):
            if board_raw[2] == " ":
                board_raw[2] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
        elif line_input in ("B", "b"):
            if board_raw[5] == " ":
                board_raw[5] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
            user_input()
        elif line_input in ("C", "c"):
            if board_raw[8] == " ":
                board_raw[8] = f"{player_turn}"
                checking_winner()
            else:
                print("Feld ist schon belegt, bitte neue Eingabe!")
                user_input()
    else:
        print("Ungültige Eingabe")
        user_input()

def checking_winner():
    global board_raw
    global player_turn
    #print("Checking_winner...")
    if board_raw[0] == f"{player_turn}" and board_raw[1] == f"{player_turn}" and board_raw[2] == f"{player_turn}":
        winner()
    elif board_raw[3] == f"{player_turn}" and board_raw[4] == f"{player_turn}" and board_raw[5] == f"{player_turn}":
        winner()
    elif board_raw[6] == f"{player_turn}" and board_raw[7] == f"{player_turn}" and board_raw[8] == f"{player_turn}":
        winner()
    elif board_raw[0] == f"{player_turn}" and board_raw[3] == f"{player_turn}" and board_raw[6] == f"{player_turn}":
        winner()
    elif board_raw[1] == f"{player_turn}" and board_raw[4] == f"{player_turn}" and board_raw[7] == f"{player_turn}":
        winner()
    elif board_raw[2] == f"{player_turn}" and board_raw[5] == f"{player_turn}" and board_raw[8] == f"{player_turn}":
        winner()
    elif board_raw[0] == f"{player_turn}" and board_raw[4] == f"{player_turn}" and board_raw[8] == f"{player_turn}":
        winner()
    elif board_raw[2] == f"{player_turn}" and board_raw[4] == f"{player_turn}" and board_raw[6] == f"{player_turn}":
        winner()
    elif " " not in board_raw:
        print("Unentschieden!")
        print(get_board_con())
        menu()
    else:
        if player_turn == "X":
            player_turn = "O"
            user_input()
        else:
            player_turn = "X"
            user_input()

def winner():
    print(f"Glückwunsch Spieler {player_turn}, du hast gewonnen!")
    print(get_board_con())
    menu()




start()