import sys
input=sys.stdin.readline

n,r,c=map(int,input().split())
visited=0

def find(x,y,n): #x,y시작점, 각 내부사각형
    global visited
    if x==r and y==c:
        print(visited)
        exit(0)
    if n==1:
        visited = visited + 1
        return
    if not (x<=r<x+n and y<=c<y+n):
        visited=visited+n*n
        return
    divide=n//2
    find(x,y,divide)
    find(x,y+divide,divide)
    find(x+divide,y,divide)
    find(x+divide,y+divide,divide)

find(0,0,2**n)
print(visited)