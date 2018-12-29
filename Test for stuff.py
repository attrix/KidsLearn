import curses
import math

s = curses.initscr()
curses.noecho()
curses.cbreak()
s.keypad(True)

r = s.getch() - 48
sx = 50
sy = 10
angle = 0
while (angle <= 360):
    rad = (6.28/360) * angle
    nx = round(math.cos(rad) * r) + sx
    ny = sy - round((math.sin(rad) * r))
    s.addch(ny,nx,'.')
    s.refresh()
    angle = angle + 5
        

        