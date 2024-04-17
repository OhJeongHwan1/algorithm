# 1로 만들기 3 골 3
# 
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
queue.append([N,0])
the_set = set()
the_set.add(N)
count = 0

while queue:
    num, cost = queue.popleft()
    count +=1
    if num == 1:
        print(cost)
        #print(count)
        break

    if num % 3 == 0:
        if num//3 not in the_set:
            queue.append([num//3,cost + 1])
            the_set.add(num//3)

    if num % 2 == 0:
        if num//2 not in the_set:
            queue.append([num//2,cost + 1])
            the_set.add(num//2)

    if num-1 not in the_set:
            queue.append([num-1,cost + 1])
            the_set.add(num-1)



