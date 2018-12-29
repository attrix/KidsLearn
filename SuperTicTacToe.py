def checkgame(column):
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


#Main program starts here

r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']
c1 = [r1,r2,r3]
c2 = [r1,r2,r3]
c3 = [r1,r2,r3]
c4 = [r1,r2,r3]
c5 = [r1,r2,r3]
c6 = [r1,r2,r3]
c7 = [r1,r2,r3]
c8 = [r1,r2,r3]
c9 = [r1,r2,r3]
supercol = [r1,r2,r3]

board = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
supergameresult = 0
player1 = 'X'
player2 = 'O'
currentgame = int(input)
checkgame(board[currentgame])

for x in range (0,9):
    print(board[x])
    if (x == 2):
        print("")
    if (x == 5):
        print("")