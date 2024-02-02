# 16236 아기 상어
# bfs 및 구현 문제
# 풀지 못함...
# 각각으로의 최단 거리를 구해서 먹을 수 있는 물고기를 선별
# 그 물고기로 이동하여 물고기를 먹은 후 거기서 다시 거리를 구함.

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

the_map = [list(map(int, input().split())) for _ in range(N)]
moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
size = 2
eat = 0

# 아기 상어의 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if the_map[i][j] == 9:
            shark_x, shark_y = i, j
            the_map[i][j] = 0

def bfs(x, y, size):
    queue = deque([(x, y)])
    dist = [[-1]*N for _ in range(N)]
    dist[x][y] = 0
    fish = []

    while queue:
        x, y = queue.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and the_map[nx][ny] <= size and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
                if 0 < the_map[nx][ny] < size:
                    fish.append((dist[nx][ny], nx, ny))
    
    if not fish:
        return None
    fish.sort()  # 거리, 가장 위, 가장 왼쪽 순으로 정렬
    return fish[0]

time = 0
while True:
    result = bfs(shark_x, shark_y, size)
    if result is None:
        break
    dist, shark_x, shark_y = result
    time += dist
    eat += 1
    the_map[shark_x][shark_y] = 0  # 물고기 먹기
    if eat == size:  # 크기만큼 물고기를 먹었다면 크기 증가
        size += 1
        eat = 0

print(time)
