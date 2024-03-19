import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for i in range(N):
    queue.append(i+1)

while queue:
    borrow = queue.popleft()
    print(borrow,end=' ')

    if queue:
        to_under = queue.popleft()
        queue.append(to_under)





