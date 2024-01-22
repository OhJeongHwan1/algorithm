#10026 실 1 적록색약
# sys.setrecursionlimit(10**6) 로 재귀 깊이 변경해주기 필요

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N = int(input())
picture = []
colors = [[0 for _ in range(N)] for _ in range(N)]
BLIND_NESS = ['R','G']

move = [[1,0],[0,1],[-1,0],[0,-1]]

def dfs(x,y,color):
    if colors[x][y] != 0:
        return

    colors[x][y] = color

    for xMove,yMove in move:
        if 0 <= x+xMove <= N-1 and 0 <= y+yMove <= N-1:
            if picture[x][y] == picture[x+xMove][y+yMove]:
                dfs(x+xMove, y+yMove, color)


# def dfs_for_blindness(x,y,color):
#     if colors[x][y] != 0:
#         return

#     colors[x][y] = color
   
#     for xMove,yMove in move:
#         if 0 <= x+xMove <= N-1 and 0 <= y+yMove <= N-1:
#             if (picture[x][y] in BLIND_NESS) and (picture[x+xMove][y+yMove] in BLIND_NESS):
#                 dfs(x+xMove, y+yMove, color)
#             if picture[x][y] == picture[x+xMove][y+yMove]:
#                 dfs(x+xMove, y+yMove, color)

for _ in range(N):
    picture.append(list(input().strip()))

num = 1

for x in range(N):
    for y in range(N):
        if colors[x][y] == 0:
            dfs(x,y,num)
            num += 1

print(max(map(max, colors)))

colors = [[0 for _ in range(N)] for _ in range(N)]


for x in range(N):
    for y in range(N):
        if picture[x][y] == 'R':
            picture[x][y] = 'G'
num = 1

for x in range(N):
    for y in range(N):
        if colors[x][y] == 0:
            dfs(x,y,num)
            num += 1

print(max(map(max, colors)))

