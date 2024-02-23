#1697 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

INF = float("inf")
N, K = map(int,input().split())

the_limit = 2*K-N
position = [ INF for _ in range(2*1000000)]
position[N] = 0

if N > K:
    print(abs(N-K))
    exit()

def find(num):
    global the_limit
    queue = deque()
    queue.append(num)

    while queue:
        n = queue.popleft()

        if 0 <= n+1 < the_limit:
            if position[n] + 1 < position[n+1]:
                position[n+1] = min(position[n] + 1,position[n+1])
                queue.append(n+1)

        if 0 <= n+1 < the_limit:
            if position[n] + 1 < position[n-1]:
                position[n-1] = min(position[n] + 1,position[n-1])
                queue.append(n-1)

        if 0 <= 2*n < the_limit:
            if position[n] + 1 < position[2*n]:
                position[2*n] = min(position[n] + 1,position[2*n])
                queue.append(2*n)
    
find(N)
print(position[K])