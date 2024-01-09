import sys

input=sys.stdin.readline

def check(myCard,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if myCard[mid] > target:
            end = mid - 1
        elif myCard[mid] < target:
            start = mid + 1
        else:
            return True
        
    return False

N = int(input())
myCard = list(map(int,(input().split())))

myCard.sort()
M = int(input())
checkCards = list(map(int,(input().split())))

for i in range(M):
    start = 0
    end = N - 1
    
    if check(myCard,checkCards[i],start,end) == True:
        print(1, end=' ')
    else:
        print(0, end=' ')

