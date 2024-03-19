# 2638 치즈 골3

import sys
from collections import deque
input = sys.stdin.readline

MOVE = [[0,-1],[-1,0],[1,0],[0,1]]
N, M = map(int,input().split())

the_map = []
result = 0

for _ in range(N):
    the_map.append(list(map(int,input().split())))

def delete():

    out_of_cheese()

    for x in range(N):
        for y in range(M):
            if the_map[x][y] == 1:
                count = 0
                for dx, dy in MOVE:
                    nx, ny = x+dx,y+dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if the_map[nx][ny] == -1:
                            count += 1

                if count >= 2:
                    the_map[x][y] = 2

    for x in range(N):
        for y in range(M):
            if the_map[x][y] == 2 or the_map[x][y] == -1:
                the_map[x][y] = 0


def out_of_cheese():
    start_x = 0
    start_y = 0
    queue = deque()

    visited = [ [False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if the_map[i][j] == 0:
                start_x = i
                start_y = j
                break

    queue.append([start_x,start_y])
    visited[start_x][start_y] = True
    while queue:
        x,y = queue.popleft()

        the_map[x][y] = -1

        for dx, dy in MOVE:
            nx, ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and the_map[nx][ny] != 1 and the_map[nx][ny] != -1:
                    queue.append([nx,ny])
                    visited[nx][ny] = True


while True:
    delete()
    result += 1
    if max(map(max,the_map)) == 0:
        break

print(result)