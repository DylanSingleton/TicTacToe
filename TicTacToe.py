import random

interface = range(0,10)
totalGames = 0

def menu():
    print("Welcome to TicTacToe. Created By Dylan Singleton\n\nStart Game\nCheck Score\nExit\n ")
    option = raw_input("What would you like to do? ")

    if option.upper() == "start game".upper():
        showBoard()
        player = random.randint(1, 2)
        if player == 1:
            playerOneInput()
        else:
            playerTwoInput()
    elif option.upper() == "check score".upper():
        updateGames(totalGames)
        fileName = "Wins.txt"
        file = open(fileName)
        score = file.read()
        print(score)
        file.close()

        raw_input("Press ENTER to return to the MENU. ")
        menu()
    elif option.upper() == "exit".upper():
            onExit()
    else:
        print("Please pick a valid option. ")
        menu()

def showBoard():
    print(interface[1]), (interface[2]), (interface[3])
    print(interface[4]), (interface[5]), (interface[6])
    print(interface[7]), (interface[8]), (interface[9])

def playerOneInput():
    playerOne = raw_input("Player one pick an area. You are 'X'. ")
    try:
        playerOne = int(playerOne)
    except ValueError:
        print("Please pick a valid area.")
        playerOneInput()
    else:
        while interface[playerOne] != 'X' and interface[playerOne] != 'O':
            interface[playerOne] = 'X'
            checkBoard()
            showBoard()
            playerTwoInput()
        else:
            print("That area has been taken! Please pick a valid area player one")
            showBoard()
            playerOneInput()

def playerTwoInput():
    playerTwo = raw_input("Player two pick an area. You are 'O'. ")
    try:
        playerTwo = int(playerTwo)
    except ValueError:
        print("Please pick a valid area.")
        playerTwoInput()
    else:
        while interface[playerTwo] != 'X' and interface[playerTwo] != 'O':
            interface[playerTwo] = 'O'
            checkBoard()
            showBoard()
            playerOneInput()
        else:
            print("That area has been taken! Please pick a valid area player two")
            showBoard()
            playerTwoInput()

def checkBoard():
    #All possible winning positions
    winPos = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3))
    #Replaces a,b,c with (1,2,3) ect...
    for a,b,c in winPos:
        #Checks to see is a,b,c = X or Y. If they do execute xWin or oWin. Otherwise check for a draw.
        if interface[a] and interface[b] and interface[c] == 'X':
            xWin()
        elif interface[a] and interface[b] and interface[c] == 'O':
            oWin()
        elif interface[1] != 1 and interface[2] != 2 and interface[3] != 3 and interface[4] != 4 and interface[5] != 5 and interface[6] != 6 and interface[7] != 7 and interface[8] != 8 and interface[9] != 9:
            gameDraw()

def xWin():
    showBoard()
    raw_input("Player ONE wins! Press ENTER to continue. ")
    fileName = "Wins.txt"
    file = open(fileName, 'a')
    file.writelines("Player ONE has won! \n")
    file.close()
    resetGame()

def oWin():
    showBoard()
    raw_input("Player TWO wins! Press ENTER to continue. ")
    fileName = "Wins.txt"
    file = open(fileName, 'a')
    file.writelines("Player TWO has won! \n")
    file.close()

    resetGame()

def updateGames(totalGames):
    totalGames += 1
    print "Games Played: ", totalGames

def gameDraw():
    showBoard()
    raw_input("The game is a DRAW! Press ENTER to continue. ")
    fileName = "Wins.txt"
    file = open(fileName, 'a')
    file.writelines("The game was a DRAW! \n")
    file.close()
    resetGame()

def resetGame():
    global interface
    interface = range(0, 10)
    menu()

def onExit():
    choice = raw_input("Are you sure you want to EXIT the game? Yes/No: ")
    if choice.upper() == "yes".upper():
        quit()
    elif choice.upper() == "no".upper():
        menu()
    else:
        print("Please pick a valid option.")
        onExit()
#Runs the menu
menu()