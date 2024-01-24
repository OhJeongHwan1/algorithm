# 최단 경로 2178 
# dfs 를 사용해서는 해결할 수 없음. 시간 복잡도가 너무 커지기 때문에

import sys

input = sys.stdin.readline
from collections import deque
# sys.setrecursionlimit(10**6)
N, M = map(int,input().split())

maze = []
dist = [[100000 for _ in range(M)] for _ in range(N)]
moves = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(N):
    maze.append(list(input().strip()))

# def search(x,y,dst):
#     if maze[x][y] == 0:
#         return
    
#     dist[x][y] = dst

#     for xM, yM in moves:
#         if 0 <= x+xM <= N-1 and 0 <= y+yM <= M-1:
#             if maze[x+xM][y+yM] == '0':
#                 continue
#             if dist[x][y] + 1 < dist[x+xM][y+yM]:
#                 search(x+xM,y+yM,dst+1)

# search(0,0,1)
    
queue = deque([[0,0]])
dist[0][0] = 1
while queue:
    x,y = queue.popleft()
    if maze[x][y] == '0':
        continue

    for xM, yM in moves:
        if 0 <= x+xM <= N-1 and 0 <= y+yM <= M-1:
            if maze[x+xM][y+yM] == '0':
                continue
            if dist[x][y] + 1 < dist[x+xM][y+yM]:
                dist[x+xM][y+yM] = dist[x][y]+1
                queue.append([x+xM,y+yM])



print(dist[N-1][M-1])
