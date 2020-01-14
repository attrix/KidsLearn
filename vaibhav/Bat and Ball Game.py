import curses
import time
import math 

s = curses.initscr()
curses.noecho()
curses.cbreak()
s.keypad(True)
curses.curs_set(0)

x = 0
y = 0
gameresult = 0
ydirection = 1
batx = 1
baty = 10
slope = math.tan(.785)
xdire = 1

while(True):
    s.addch(y,x, 'o')
    s.refresh()
    time.sleep(0.1)
    s.addch(y,x,' ')
    time.sleep(0.1)
    s.refresh()
    y = y + ydirection
    x = x + (xdire * int(1 / slope))

    if (y >10):
        ydirection = ydirection * -1
    
    if (y < 1):
        ydirection = ydirection * -1

    if (x<1):
        xdire = xdire * -1
        curses.beep()
   
    if (x > 50):
        xdire = xdire * -1
        curses.beep()

