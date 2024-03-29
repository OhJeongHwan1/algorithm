# 11559 뿌요뿌요 골4 구현

import sys
input = sys.stdin.readline
from collections import deque
MOVE = [[0,1],[1,0],[0,-1],[-1,0]]
field = []
result = 0

for _ in range(12):
    field.append(list(map(str,input().strip())))

def check_puyo(x,y):
    count = 1
    visited = [[False for _ in range(6)] for _ in range(12)]
    queue = deque()

    queue.append([x,y])
    visited[x][y] = True
    while queue:
        sx,sy = queue.popleft()

        for dx, dy in MOVE:
            nx,ny = sx+dx,sy+dy
            if 0 <= nx < 12 and 0 <= ny < 6:
                if visited[nx][ny] == False and field[x][y] == field[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    count += 1

    if count >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j] == True:
                    field[i][j] = '.'

        return True
    
    return False

def down():
    for x in range(10,-1,-1):
        for y in range(5,-1,-1):
            if field[x][y] !='.' and field[x+1][y] == '.':
                field[x+1][y] = field[x][y]
                field[x][y] ='.'
while True:
    count = 0
    for i in range(12):
        for j in range(6):
            if field[i][j] !='.':
                if check_puyo(i,j) == True:
                    count += 1
    if count == 0:
        break
    
    # for i in range(12):
    #     for j in range(6):
    #         print(field[i][j],end='')
    #     print()
    # print('-------------------------------')
    down()
    down()
    down()
    down()
    down()
    down()
    down()
    down()
    down()
    down()
    down()

    # for i in range(12):
    #     for j in range(6):
    #         print(field[i][j],end='')
    #     print()
    # print('-------------------------------')
    result += 1

# for i in range(12):
#     for j in range(6):
#         print(field[i][j],end='')
#     print()

print(result)