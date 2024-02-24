# 13913 숨바꼭질 4

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = float("inf")
N, K = map(int,input().split())

THE_LIMIT = 100001
position = [ INF for _ in range(THE_LIMIT)]
position[N] = 0
route_array = [ 0  for _ in range(THE_LIMIT)]
path = []

if N > K:
    print(abs(N-K))
    for i in range(N,K-1,-1):
        print(i, end=' ')
    exit()

def find(num):
    queue = deque()
    queue.append(num)

    while queue:
        n = queue.popleft()

        for nx in (n+1,n-1,2*n):
            if 0 <= nx < THE_LIMIT:
                if position[n] + 1 <= position[nx]:
                    position[nx] = min(position[n] + 1,position[nx])
                    queue.append(nx)
                    route_array[nx] = n

find(N)
print(position[K])
path.append(K)
temp = route_array[K]
for i in range(position[K]):
    path.append(temp)
    temp = route_array[temp]

print(*path[::-1])