import curses


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


s = curses.initscr()
curses.noecho()
curses.cbreak()
s.keypad(True)
x = 0
y = 0
s.addstr(y,x," | | ",curses.A_UNDERLINE)
y = y+1
s.addstr(y,x," | | ",curses.A_UNDERLINE)
y = y+1
s.addstr(y,x," | | ")
x = 0
y = 0
s.move(y,x)
player1 = 'X'
player2 = 'O'
player = player1
gameresult = 0
r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']  
board = [r1,r2,r3]

while( gameresult == 0):
    inp = s.getch()
    if (inp == curses.KEY_LEFT):
        x = x - 2
        if (x <0):
            x = 0
            curses.beep()
        
    elif (inp == curses.KEY_RIGHT):
        x = x + 2
        if(x>4):
            x = 4
            curses.beep()
    elif (inp == curses.KEY_UP):
        y = y-1
        if(y<0):
            y = 0
            curses.beep()
    elif (inp == curses.KEY_DOWN):
        y = y+1
        if (y>2):
            y = 2
            curses.beep()
    
    elif (inp == 32):
        boardx = int(x/2)
        boardy = int(y)
        if (board[boardy][boardx] == ' '):
            s.addch(y,x,player)
            board[boardy][boardx] = player
            gameresult = checkgame(board)
            if (gameresult == 1):
                s.addstr(5,0,"YAY! PLAYER 1 WON!")
                curses.beep()
                curses.beep()
                
            elif (gameresult == 2):
                s.addstr(5,0,"YAY! PLAYER 2 WON!")
                curses.beep()
                curses.beep()

            elif (gameresult == 3):
                s.addstr(5,0,"GAME DRAWN!!")
                curses.beep()
                curses.beep()
                        
            if (player == player1):
                player = player2
            else:
                player = player1
        else:
            curses.beep()
    
    s.move(y,x)

s.getch()