import sys

xstr = input("Enter first number: ")
ystr = input("Enter second number: ")

x = int(xstr)
y = int(ystr)
op = input("Enter operation (*,/,+,-): ")
ans = 0
if (op == "*"):
    ans = x * y
elif (op == "/"):
    ans = x / y
elif (op == "+"):
    ans = x + y
elif (op == "-"):
    ans = x - y
print(ans)