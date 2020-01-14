
player1 = 'X'
player2 = 'O'
player = player1
currentplayer = 0
gameresult = 0 # 0 = no result, 1 = player 1 won, 2 = player 2 won, 3 = draw
r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']
column = [r1,r2,r3]   

def checkgame():
    #Defining if the player won in terms of columns  
    if ((column[0][0] == column[1][0]) and (column[0][0] == column[2][0])):
        if (column[0][0] == 'X'):
            return 1
        elif (column[0][0] == 'O'):
            return 2
    if ((column[0][1] == column[1][1]) and (column[0][1] == column[2][1])):
        if (column[0][1] == 'X'):
            return 1
        elif (column[0][1] == 'O'):
            return 2
    if ((column[0][2] == column[1][2]) and (column[0][2] == column[2][2])):
        if (column[0][2] == 'X'):
            return 1
        elif (column[0][2] == 'O'):
            return 2
         #   Defining if the player won in terms of rows 
    if ((column[0][0] == column[0][1]) and (column[0][0] == column[0][2])):
        if (column[0][0] == 'X'):
            return 1
        elif (column[0][0] == 'O'):
            return 2
    if ((column[1][0] == column[1][1]) and (column[1][0] == column[1][2])):
        if (column[1][0] == 'X'):
            return 1
        elif (column[1][0] == 'O'):
            return 2
    if ((column[2][0] == column[2][1]) and (column[2][0] == column[2][2])):
        if (column[2][0] == 'X'):
            return 1
        elif (column[2][0] == 'O'):
            return 2
        #Defining if the player won in terms of diagonals
    if ((column[0][0] == column[1][1]) and (column[0][0] == column[2][2])):
        if (column[0][0] == 'X'):
            return 1
        elif (column[0][0] == 'O'):
            return 2
    if ((column[0][2] == column[1][1]) and (column[0][2] == column[2][0])):
        if (column[0][2] == 'X'):
            return 1
        elif (column[0][2] == 'O'):
            return 2

    #Check if we can continue
    i = 0
    j = 0
    for i in range(0,3):
        for j in range(0,3):
            if (column[i][j] == ' '):
                return 0
    
    return 3

while gameresult == 0:
    print("player " + player +" turn")
    print(column[0])
    print(column[1])
    print(column[2])
    x = int(input("Give x:"))-1
    y = int(input("Give y:"))-1
    if ((x>2) or (y>2)):
        print ("Not a valid move")
        continue 
            
    if (column[x][y] == ' '):
        column[x][y] = player
   
    
    gameresult = checkgame()

    if (gameresult == 0):
        if (player == player1):
            player = player2
        else:
            player = player1 
    elif (gameresult == 1):
        print("YAY! PLAYER 1 WON!")
    elif (gameresult == 2):
        print("YAY! PLAYER 2 WON!")
    elif (gameresult == 3):
        print("NOOOOOOOOOOOO!NO ONE WON!")

    else:
        print("Space Taken!")