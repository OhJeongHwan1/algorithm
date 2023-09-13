import sys

n = int(input())
tree = []
for i in range(n):
    tree.append(list(map(int,sys.stdin.readline().split())))
num0 = 0
num1 = 0
num2 = 0


def paper(x,y,n):
    global num0, num1, num2
    first = tree[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != tree[i][j]:
                divide = n //3
                paper(x,y,divide)
                paper(x, y+divide, divide)
                paper(x, y+2*divide, divide)
                paper(x+divide, y, divide)
                paper(x+divide,y+divide,divide)
                paper(x+divide, y+2*divide, divide)
                paper(x+2*divide, y,divide)
                paper(x+2*divide, y+divide, divide)
                paper(x+2*divide,y+2*divide,divide)
                return

    if(first == -1):
        num0 = num0 + 1
    elif(first == 0):
        num1 = num1 + 1
    elif(first == 1):
        num2 = num2 + 1
    return
    

paper(0,0,n)
print(num0,end='\n')
print(num1,end='\n')
print(num2,end='\n')