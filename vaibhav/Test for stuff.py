n = int(input("Give me the number: "))
width = n
length = n-1
def tri(n):
    for i in range (0,n-1):
        print(" "*(n-i-2)+"/"*(i+1)+"**"+"\\"*(i+1))
    
def square(n):
    for i in range(1,n+1):
        print("|"+"."*(2*n-1)+"|")
def line (n):
    print("+"+"%*"*(n-1)+"%+")
tri(n)
line(n)
square(n)
line(n)
square(n)
line(n)
tri(n)
