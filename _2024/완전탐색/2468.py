# 2468 안전 영역

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

area = []
rain_deep = [ 0 for _ in range(101)]
move = [[1,0],[0,1],[-1,0],[0,-1]]

for _ in range(N):
    area.append(list(map(int,input().split())))

def number_of_area(num):
    visited = [[False for _ in range(N)] for _ in range(N)]
    the_number = 0

    for i in range(N):
        for j in range(N):
            if area[i][j] > num and not visited[i][j]:
                queue = deque()
                queue.append([i, j])
                visited[i][j] = True
                the_number += 1

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if area[nx][ny] > num and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append([nx, ny])
    return the_number


the_highest = max(map(max,area))

for i in range(0,the_highest):
    rain_deep[i] = number_of_area(i)


print(max(rain_deep))