# 1941 소문난 칠공주 골1
# 완전 탐색

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
MOVE = [[0,1],[1,0],[0,-1],[-1,0]]
the_class = [list(map(str,input().strip())) for _ in range(5)]
ans = 0

cos = []
for i in range(5):
    for j in range(5):
        cos.append([i,j])

def checkSeven(comb):
    cnt = 0 
    for x,y in comb:
        if the_class[x][y] == 'S':
            cnt += 1

    return True if cnt >= 4 else False

def bfs(comb):
    global ans
    visited = [ False for _ in range(7) ]
    queue = deque()
    queue.append(comb[0])
    visited[0] = True

    while queue:
        x,y = queue.popleft()

        for dx,dy in MOVE:
            nx = dx + x
            ny = dy + y
            if [nx,ny] in comb:
                nextIdx = comb.index([nx, ny])
                if visited[nextIdx] == False:
                    queue.append([nx,ny])
                    visited[nextIdx] = True
    if False not in visited:
        ans += 1

for comb in list(combinations(cos,7)):
    if checkSeven(comb):
        bfs(comb)

print(ans)