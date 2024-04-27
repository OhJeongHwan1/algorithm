# 13459 구슬 탈출 골1
import sys
from collections import deque
input=sys.stdin.readline

N,M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]


for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            x = i
            y = j

        if board[i][j] == 'B':
            blue_x = i
            blue_y = j
queue = deque()
queue.append([x,y,0])

while queue:
    x,y,time = queue.popleft()
