import sys

input=sys.stdin.readline

def neverChange(x,y):
    if(int(y/x * 100) == 99):
        return True
    if(x == y):
        return True
    
    return False

X, Y = map(int,(input().split()))

Z = int(Y*100/X)

if neverChange(X,Y) == True:
    print(-1)
    exit()

answer = 0
start = 1
end = X

while start <= end:
    mid = (start+end)//2

    if (Y+mid) * 100// (X+mid)  <= Z:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid


print(answer)
