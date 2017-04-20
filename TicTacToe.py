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
        onLoad()
    elif option == 2:
        checkScore()
    elif option == 3:
        onQuit()
    else:
        menu()

def showBoard():
    print(interface[1]), (interface[2]), (interface[3])
    print(interface[4]), (interface[5]), (interface[6])
    print(interface[7]), (interface[8]), (interface[9])

def playerOneInput():
    playerOne = input("Player ONE pick an area. You are 'x'. ")
    playerOne = int(playerOne)
    while interface[playerOne] != 'x' and interface[playerOne] != 'o':
        interface[playerOne] = 'x'
        checkBoard()
        showBoard()
        playerTwoInput()
    else:
        print("That area has been taken! Please pick a valid area PLAYER ONE")
        showBoard()
        playerOneInput()

def playerTwoInput():
    playerTwo = input("Player TWO pick an area. You are 'o'. ")
    playerTwo = int(playerTwo)
    while interface[playerTwo] != 'x' and interface[playerTwo] != 'o':
        interface[playerTwo] = 'o'
        checkBoard()
        showBoard()
        playerOneInput()
    else:
        print("That area has been taken! Please pick a valid area PLAYER TWO")
        showBoard()
        playerTwoInput()

def checkBoard():
    #Horizontal x
    if interface[1] == 'x' and interface[2] == 'x' and interface[3] == 'x':
        xWin()
    elif interface[4] == 'x' and interface[5] == 'x' and interface[6] == 'x':
        xWin()
    elif interface[7] == 'x' and interface[8] == 'x' and interface[9] == 'x':
        xWin()

    #Vertical x
    elif interface[1] == 'x' and interface[4] == 'x' and interface[7] == 'x':
        xWin()
    elif interface[2] == 'x' and interface[5] == 'x' and interface[8] == 'x':
        xWin()
    elif interface[3] == 'x' and interface[6] == 'x' and interface[9] == 'x':
        xWin()

    #Diagnal x
    elif interface[1] == 'x' and interface[5] == 'x' and interface[9] == 'x':
        xWin()
    elif interface[7] == 'x' and interface[5] == 'x' and interface[3] == 'x':
        xWin()

    #Horizontal o
    elif interface[1] == 'o' and interface[2] == 'o' and interface[3] == 'o':
        oWin()
    elif interface[4] == 'o' and interface[5] == 'o' and interface[6] == 'o':
        oWin()
    elif interface[7] == 'o' and interface[8] == 'o' and interface[9] == 'o':
        oWin()

    #Vertical o
    elif interface[1] == 'o' and interface[4] == 'o' and interface[7] == 'o':
        oWin()
    elif interface[2] == 'o' and interface[5] == 'o' and interface[8] == 'o':
        oWin()
    elif interface[3] == 'o' and interface[6] == 'o' and interface[9] == 'o':
        oWin()

    #Diagnal o
    elif interface[1] == 'o' and interface[5] == 'o' and interface[9] == 'o':
        oWin()
    elif interface[7] == 'o' and interface[5] == 'o' and interface[3] == 'o':
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
    raw_input("The game is a DRAW!! Press ENTER to continue. ")
    fileName = "Wins.txt"
    file = open(fileName, 'a')
    file.writelines("GAME DRAW!! \n")
    file.close()
    resetGame()

def resetGame():
    global interface
    interface = range(0, 10)
    menu()

def checkScore():
    fileName = "Wins.txt"
    file = open(fileName)
    score = file.read()
    print(score)
    file.close()

    raw_input("Press ENTER to return to the MENU. ")
    menu()

def onLoad():
    showBoard()
    player = random.randint(1,2)
    if player == 1:
        playerOneInput()
    else:
        playerTwoInput()

def onQuit():
   #Range of YES inputs that close the game
   inputYes = ['Yes','yes','Y','y']
   #Range of NO inputs that close the game
   inputNo = ['No','no','N','n']
   #Prints out insturctions for the user
   print("Use", inputYes , "QUIT.")
   print("Use", inputNo , "to go back to the MENU.")
   #Gets the users input and makes a choice based on it
   choice = raw_input("Are you sure you want to EXIT the game? ")
   if choice in inputYes:
            quit()
   elif choice in inputNo:
       menu()
   else:
       print("Please pick a valid option. ")
       onQuit()

#Runs the menu
menu()