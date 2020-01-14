#Main program starts here
r1 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r2 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r3 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r4 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r5 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r6 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r7 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r8 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
r9 = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
biggy = [' ',' ',' ',' ',' ',' ',' ', ' ',' ']
player1 = 'X'
player2 = 'O'
m = [r1,r2,r3,r4,r5,r6,r7,r8,r9] # m stands for mini board
b = [biggy] # b stands for big board
currentplayer = player1
def printBoard():
        GameBoard='''
                           2                 3
|¯¯¯|¯¯¯|¯¯¯| |¯¯¯|¯¯¯|¯¯¯| |¯¯¯|¯¯¯|¯¯¯|
| '''+m[0][0]+''' | '''+m[0][1]+''' | '''+m[0][2]+''' | | '''+m[1][0]+''' | '''+m[1][1]+''' | '''+m[1][2]+''' | | '''+m[2][0]+''' | '''+m[2][1]+''' | '''+m[2][2]+''' |
|___|___|___| |___|___|___| |___|___|___|
|   |   |   | |   |   |   | |   |   |   |
| '''+m[0][3]+''' | '''+m[0][4]+''' | '''+m[0][5]+''' | | '''+m[1][3]+''' | '''+m[1][4]+''' | '''+m[1][5]+''' | | '''+m[2][3]+''' | '''+m[2][4]+''' | '''+m[2][5]+''' |
|___|___|___| |___|___|___| |___|___|___|
|   |   |   | |   |   |   | |   |   |   |
| '''+m[0][6]+''' | '''+m[0][7]+''' | '''+m[0][8]+''' | | '''+m[1][6]+''' | '''+m[1][7]+''' | '''+m[1][8]+''' | | '''+m[2][6]+''' | '''+m[2][7]+''' | '''+m[2][8]+''' |
|___|___|___| |___|___|___| |___|___|___|
          4                 5                 6
|¯¯¯|¯¯¯|¯¯¯| |¯¯¯|¯¯¯|¯¯¯| |¯¯¯|¯¯¯|¯¯¯|
| '''+m[3][0]+''' | '''+m[3][1]+''' | '''+m[3][2]+''' | | '''+m[4][0]+''' | '''+m[4][1]+''' | '''+m[4][2]+''' | | '''+m[5][0]+''' | '''+m[5][1]+''' | '''+m[5][2]+''' |
|___|___|___| |___|___|___| |___|___|___|
|   |   |   | |   |   |   | |   |   |   |
| '''+m[3][3]+''' | '''+m[3][4]+''' | '''+m[3][5]+''' | | '''+m[4][3]+''' | '''+m[4][4]+''' | '''+m[4][5]+''' | | '''+m[5][3]+''' | '''+m[5][4]+''' | '''+m[5][5]+''' |
|___|___|___| |___|___|___| |___|___|___|
|   |   |   | |   |   |   | |   |   |   |
| '''+m[3][6]+''' | '''+m[3][7]+''' | '''+m[3][8]+''' | | '''+m[4][6]+''' | '''+m[4][7]+''' | '''+m[4][8]+''' | | '''+m[5][6]+''' | '''+m[5][7]+''' | '''+m[5][8]+''' |
|___|___|___| |___|___|___| |___|___|___|
          7                 8                 9
|¯¯¯|¯¯¯|¯¯¯| |¯¯¯|¯¯¯|¯¯¯| |¯¯¯|¯¯¯|¯¯¯|
| '''+m[6][0]+''' | '''+m[6][1]+''' | '''+m[6][2]+''' | | '''+m[7][0]+''' | '''+m[7][1]+''' | '''+m[7][2]+''' | | '''+m[8][0]+''' | '''+m[8][1]+''' | '''+m[8][2]+''' |
|___|___|___| |___|___|___| |___|___|___|
|   |   |   | |   |   |   | |   |   |   |
| '''+m[6][3]+''' | '''+m[6][4]+''' | '''+m[6][5]+''' | | '''+m[7][3]+''' | '''+m[7][4]+''' | '''+m[7][5]+''' | | '''+m[8][3]+''' | '''+m[8][4]+''' | '''+m[8][5]+''' |
|___|___|___| |___|___|___| |___|___|___|
|   |   |   | |   |   |   | |   |   |   |
| '''+m[6][6]+''' | '''+m[6][7]+''' | '''+m[6][8]+''' | | '''+m[7][6]+''' | '''+m[7][7]+''' | '''+m[7][8]+''' | | '''+m[8][6]+''' | '''+m[8][7]+''' | '''+m[8][8]+''' |
|___|___|___| |___|___|___| |___|___|___|
'''
        print(GameBoard)


def minicheckgame():
    #Defining if the player won in terms of ms  
    if ((m[0][0] == m[1][0]) and (m[0][0] == m[2][0])):
        if (m[0][0] == 'X'):
            return 1
        elif (m[0][0] == 'O'):
            return 2
    if ((m[0][1] == m[1][1]) and (m[0][1] == m[2][1])):
        if (m[0][1] == 'X'):
            return 1
        elif (m[0][1] == 'O'):
            return 2
    if ((m[0][2] == m[1][2]) and (m[0][2] == m[2][2])):
        if (m[0][2] == 'X'):
            return 1
        elif (m[0][2] == 'O'):
            return 2
         #   Defining if the player won in terms of rows 
    if ((m[0][0] == m[0][1]) and (m[0][0] == m[0][2])):
        if (m[0][0] == 'X'):
            return 1
        elif (m[0][0] == 'O'):
            return 2
    if ((m[1][0] == m[1][1]) and (m[1][0] == m[1][2])):
        if (m[1][0] == 'X'):
            return 1
        elif (m[1][0] == 'O'):
            return 2
    if ((m[2][0] == m[2][1]) and (m[2][0] == m[2][2])):
        if (m[2][0] == 'X'):
            return 1
        elif (m[2][0] == 'O'):
            return 2
        #Defining if the player won in terms of diagonals
    if ((m[0][0] == m[1][1]) and (m[0][0] == m[2][2])):
        if (m[0][0] == 'X'):
            return 1
        elif (m[0][0] == 'O'):
            return 2
    if ((m[0][2] == m[1][1]) and (m[0][2] == m[2][0])):
        if (m[0][2] == 'X'):
            return 1
        elif (m[0][2] == 'O'):
            return 2



    