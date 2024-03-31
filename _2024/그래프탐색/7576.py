# 골5 토마토 백 그래프 dp

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
MOVE = [[0,1],[1,0],[0,-1],[-1,0]]

the_map = []
visited = [[False for _ in range(N)] for _ in range(M)]

for _ in range(M):
    the_map.append(list(map(int,input().split())))

# def check():

#     for x in range(M):
#         for y in range(N):
#             if the_map[x][y] == 0:
#                 count = 0
#                 for dx, dy in MOVE:
#                     nx, ny  = x+dx,y+dy
#                     if 0<= nx < M and 0<= ny < N:
#                         if the_map[nx][ny] == -1:
#                             count += 1
#                     else:
#                         count += 1
                
#                 if count == 4:
#                     print(-1)
#                     exit()

# check()

queue = deque()

for x in range(M):
    for y in range(N):
        if the_map[x][y] == 1:
            queue.append([x,y])
            visited[x][y] = True

while queue:
    x, y = queue.popleft()

    for dx, dy in MOVE:
        nx,ny = x+dx,y+dy
        if 0<= nx < M and 0<= ny < N:
            if visited[nx][ny] == False and the_map[nx][ny] == 0:
                the_map[nx][ny] = the_map[x][y] + 1
                queue.append([nx,ny])
                visited[nx][ny] = True

for x in range(M):
    for y in range(N):
        if the_map[x][y] == 0:
            print(-1)
            exit()

print(max(map(max,the_map)) - 1)