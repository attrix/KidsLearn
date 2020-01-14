import curses
import os

if __name__ == "__main__":
    s = curses.initscr()
    curses.cbreak()
    s.keypad(True)

    player1 = 'X'
    player2 = 'O'
    player = player1
    y = 0
    x = 0
    startx = 0
    starty = 0
    bno = 0
    gamerunning = True
    msgy = 25# where the message is printed(y)
    msgx = 0

    s.clear()
    gameboard = '''
    |---|---|---| |---|---|---| |---|---|---|
    | '''(0,0)'''  |'''(1,0)'''   |  '''(2,0)'''  | |  '''(3,0)'''  |  '''(4,0)'''  |  '''(5,0)'''  | |  '''(6,0)'''  |   '''(7,0)''' |   '''(8,0)''' |
    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|

    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|

    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|
    |   |   |   | |   |   |   | |   |   |   |
    |---|---|---| |---|---|---| |---|---|---|
    '''
    print (gameboard)

    msg = "Current board no is " + str(bno)
    curses.setyx(msgy,msgx)
    print(msg)

    