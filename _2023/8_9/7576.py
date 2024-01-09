import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
tomato = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
answer, t = 0, 0
for i in range(N):
    _list = list(map(int, input().split()))
    for j in range(M):
        tomato[i][j] = _list[j]
        if _list[j] == 1:
            q.append([i,j])
def bfs():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while q:
        _list = q.popleft()
        y, x = _list[0], _list[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if tomato[ny][nx] == 0:
                    tomato[ny][nx] = tomato[y][x] + 1
                    q.append([ny, nx])
bfs()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            t = -1
        if t != -1 and answer < tomato[i][j]:
            answer = tomato[i][j]
if t == -1:
    print(t)
else:
    print(answer-1)