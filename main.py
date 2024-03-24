
winningplayer = ""
activeplayer = winningplayer
nowinner = True
one = False
two = False
first = True
courentplayer = "X"
activeplayer = "O"
userinput = ""

field =["",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8","9"]
def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])
    return ""


player1 = input("please Enter the first Username")
player2 = input("please Enter the second Username")

def playerturn():
    global courentplayer
    global activeplayer
    if activeplayer == "O":
        activeplayer = "X"
        courentplayer = player1
    elif activeplayer == "X":
        activeplayer = "O"
        courentplayer = player2


def playerinput():
    if nowinner:
        global userinput
        print(print_field())
        userinput = input(courentplayer + " please enter a Number: ")
        userinput = int(userinput)



def normalturn():
    if nowinner:
        playerturn()
        playerinput()
        global userinput
        if field[userinput] == "X":
            usedfield()
        elif field[userinput] == "O":
            usedfield()
        else:
            field[userinput] = activeplayer




def checkdraw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != "5" and field[6] != "6" and field[7] != "7" and field[8] != "8" and field[9] != "9":
        print("no one has won, the game will be restarted")
        normalturn()



def usedfield():
    print("Please select another field that has already been selected by")
    normalturn()

while True:
    userinput = str(userinput)
    if (field[1] == field[2] == field[3] or
        field[4] == field[5] == field[6] or
        field[7] == field[8] == field[9] or
        field[1] == field[4] == field[7] or
        field[2] == field[5] == field[8] or
        field[3] == field[6] == field[9] or
        field[1] == field[5] == field[9] or
        field[3] == field[5] == field[7]):
        print(courentplayer + " has won")
        nowinner = False
        print_field()
        break

    else:
        checkdraw()
        normalturn()

