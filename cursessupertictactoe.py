import curses

s = curses.initscr()
curses.cbreak()
s.keypad(True)
xincrease = 6
yincrease = 4
yorigin = 0
player1 = 'X'
player2 = 'O'
player = player1
y = 0
x = 0
for i in range(0,3):
    for j in range(0,3):
        s.addstr(y, x, " | | ", curses.A_UNDERLINE) 
        y = y+1
        s.addstr(y, x, " | | ", curses.A_UNDERLINE)
        y = y+1
        s.addstr(y,x," | | ")
        x = x+xincrease
        y = yorigin
    yorigin = yorigin+yincrease
    y = yorigin
    x=0

s.refresh()
 
x = 0
y = 0
s.move(y,x)
while(True):
    inp = s.getch()
    if (inp == curses.KEY_RIGHT):
        x = x+2
        if (x > 16):
            x = 16
            curses.beep()
        s.move(y,x)
    
    if (inp == curses.KEY_LEFT):
        x = x-2
        if (x<0):
            x = 0
            curses.beep()
        s.move(y,x)

    if (inp == curses.KEY_UP):
        y = y-1
        if (y>0):
            y = 0
            curses.beep()
        s.move(y,x)
    
    if (inp == curses.KEY_DOWN):
        y = y+1
        if (y<11):
            y = 11
            curses.beep()
        s.move(y,x)
            




s.getch()