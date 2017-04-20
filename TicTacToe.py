import random

interface = range(0,10)

def menu():
    print("--------------------------------------------------------------------------------")
    print("            Welcome to my TicTacToe game. Created by Dylan Singleton            ")
    print("--------------------------------------------------------------------------------")
    print("Press 1: to START GAME. ")
    print("Press 2: To CHECK SCORE. ")
    print("Press 3: To EXIT GAME. ")
    option = input("Please select one: ")

    if option == 1:
        showBoard()
        player = random.randint(1, 2)
        if player == 1:
            playerOneInput()
        else:
            playerTwoInput()
    elif option == 2:
        fileName = "Wins.txt"
        file = open(fileName)
        score = file.read()
        print(score)
        file.close()

        raw_input("Press ENTER to return to the MENU. ")
        menu()
    elif option == 3:

        choice = raw_input("Are you sure you want to EXIT the game? Yes/No:  ")

        if choice.upper() == "yes".upper():
            quit()
        elif choice.upper() == "no".upper():
            menu()
        else:
            print("Please pick a valid option. ")
    else:
        menu()

def showBoard():
    print(interface[1]), (interface[2]), (interface[3])
    print(interface[4]), (interface[5]), (interface[6])
    print(interface[7]), (interface[8]), (interface[9])

def playerOneInput():
    playerOne = input("Player ONE pick an area. You are 'X'. ")
    playerOne = int(playerOne)
    while interface[playerOne] != 'X' and interface[playerOne] != 'O':
        interface[playerOne] = 'X'
        checkBoard()
        showBoard()
        playerTwoInput()
    else:
        print("That area has been taken! Please pick a valid area PLAYER ONE")
        showBoard()
        playerOneInput()

def playerTwoInput():
    playerTwo = input("Player TWO pick an area. You are 'O'. ")
    playerTwo = int(playerTwo)
    while interface[playerTwo] != 'X' and interface[playerTwo] != 'O':
        interface[playerTwo] = 'O'
        checkBoard()
        showBoard()
        playerOneInput()
    else:
        print("That area has been taken! Please pick a valid area PLAYER TWO")
        showBoard()
        playerTwoInput()

def checkBoard():
    #Horizontal x
    if interface[1] == 'X' and interface[2] == 'X' and interface[3] == 'X':
        xWin()
    elif interface[4] == 'X' and interface[5] == 'X' and interface[6] == 'X':
        xWin()
    elif interface[7] == 'X' and interface[8] == 'X' and interface[9] == 'X':
        xWin()

    #Vertical x
    elif interface[1] == 'X' and interface[4] == 'X' and interface[7] == 'X':
        xWin()
    elif interface[2] == 'X' and interface[5] == 'X' and interface[8] == 'X':
        xWin()
    elif interface[3] == 'X' and interface[6] == 'X' and interface[9] == 'X':
        xWin()

    #Diagnal x
    elif interface[1] == 'X' and interface[5] == 'x' and interface[9] == 'X':
        xWin()
    elif interface[7] == 'X' and interface[5] == 'x' and interface[3] == 'X':
        xWin()

    #Horizontal o
    elif interface[1] == 'O' and interface[2] == 'O' and interface[3] == 'O':
        oWin()
    elif interface[4] == 'O' and interface[5] == 'O' and interface[6] == 'O':
        oWin()
    elif interface[7] == 'O' and interface[8] == 'O' and interface[9] == 'O':
        oWin()

    #Vertical o
    elif interface[1] == 'O' and interface[4] == 'O' and interface[7] == 'O':
        oWin()
    elif interface[2] == 'O' and interface[5] == 'O' and interface[8] == 'O':
        oWin()
    elif interface[3] == 'O' and interface[6] == 'O' and interface[9] == 'O':
        oWin()

    #Diagnal o
    elif interface[1] == 'O' and interface[5] == 'O' and interface[9] == 'o':
        oWin()
    elif interface[7] == 'O' and interface[5] == 'O' and interface[3] == 'o':
        oWin()

    #Draw
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

#Runs the menu
menu()