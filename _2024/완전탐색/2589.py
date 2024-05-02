# 2589 보물섬 골4
import sys
from collections import deque
input = sys.stdin.readline

MOVE = [[0,1],[1,0],[-1,0],[0,-1]]
L,W = map(int,input().split())
travel_map = [list(map(str,input().strip())) for _ in range(L)]
ans = 0

def bfs(x,y):
    global ans
    visited = [[-1 for _ in range(W)] for _ in range(L)]
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 0

    while queue:
        cx,cy = queue.popleft()

        for dx,dy in MOVE:
            nx,ny = cx+dx,cy+dy
            if 0 <= nx < L and 0 <= ny < W:
                if visited[nx][ny] == -1 and travel_map[nx][ny] == 'L':
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append([nx,ny])

    return max(map(max,visited))

for i in range(L):
    for j in range(W):
        if travel_map[i][j] == 'L':
            ans = max(ans,bfs(i,j))

print(ans)