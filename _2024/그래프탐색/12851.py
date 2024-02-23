# 12851 숨바꼭질 2

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = float("inf")
N, K = map(int,input().split())

the_limit = 2*K-N
position = [ INF for _ in range(200000)]
visit = [ 0  for _ in range(200000)]
position[N] = 0

if N > K:
    print(abs(N-K))
    print("1")
    exit()

def find(num):
    global the_limit
    queue = deque()
    queue.append(num)
    visit[num] = 1

    while queue:
        n = queue.popleft()

        for nx in (n+1,n-1,2*n):
            if 0 <= nx < the_limit:
                if position[n] + 1 < position[nx]:
                    position[nx] = min(position[n] + 1,position[nx])
                    visit[nx] = visit[n]
                    queue.append(nx)
                elif position[n] + 1 == position[nx]:
                    position[nx] = min(position[n] + 1,position[nx])
                    visit[nx] += visit[n]
    
find(N)

print(position[K])
print(visit[K])