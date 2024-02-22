# 1520 내리막길
# dfs 와 dp 의 조합
# 경로를 구해야하는 문제이기 때문에 dfs 로 접근해야 함.

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

the_map = [ list(map(int,input().split())) for _ in range(N)]
dp_map = [ [-1 for _ in range(M) ] for _ in range(N)]

move = [[0,-1],[0,1],[-1,0],[1,0]]

def dfs(x,y):
    if x == N-1 and y == M-1:
        return 1
    
    if dp_map[x][y] == -1:
        dp_map[x][y] = 0

        for dx, dy in move:
            nx,ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if the_map[x][y] > the_map[nx][ny]:
                    dp_map[x][y] += dfs(nx,ny)

    return dp_map[x][y]

print(dfs(0,0))