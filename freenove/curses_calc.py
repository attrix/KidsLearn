import curses 
s = curses.initscr()
curses.noecho()
curses.cbreak()
s.keypad(True)
y = 0
x = 0

inp1 = int(s.getch())- 48
inp = int(s.getch()) - 48

for u in range (x, inp):
    s.addch(y,u, '#')
    

for i in range (y, inp1):
    s.addch(i,x,'#')
    s.refresh()
y = inp1


for u in range (0, inp):
    s.addch(y,u, '#')
    s.refresh()

x = inp-1

for i in range (0, inp1):
    s.addch(i,x,'#')        
s.refresh()
s.getch()

