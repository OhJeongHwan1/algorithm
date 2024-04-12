# 벽 부수고 이동하기 골 3
# bfs 

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
MOVE = [[0,1],[1,0],[0,-1],[-1,0]]
INF = float('inf')
the_map = []
dist = [[INF for _ in range(M)] for _ in range(N)]

for _ in range(N):
    the_map.append(list(input().strip()))

queue = deque()
queue.append([0,0,0])
dist[0][0] = 1

while queue:
    x, y, number_of_wall = queue.popleft()
    
    for dx, dy in MOVE:
        cost = number_of_wall
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if the_map[nx][ny] == '1':
                cost += 1

            if dist[x][y] + 1 < dist[nx][ny] and cost <= 1:
                queue.append([nx,ny,cost])
                dist[nx][ny] = dist[x][y] + 1

result = dist[N-1][M-1]

queue2 = deque()
queue2.append([N-1,M-1,0])
dist = [[INF for _ in range(M)] for _ in range(N)]
dist[N-1][M-1] = 1

while queue2:
    x, y, number_of_wall = queue2.popleft()
        
    for dx, dy in MOVE:
        cost = number_of_wall
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if the_map[nx][ny] == '1':
                cost += 1

            if dist[x][y] + 1 < dist[nx][ny] and cost <= 1:
                queue2.append([nx,ny,cost])
                dist[nx][ny] = dist[x][y] + 1

if dist[0][0] < result:
    result = dist[0][0]

if result == INF:
    print(-1)
else:
    print(result)
