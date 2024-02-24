# 3109 빵집
# dfs 활용하는 방법에 대해서 숙지하기

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R,C = map(int,input().split())

the_map = [list(input().strip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
moves = [[-1,1],[0,1],[1,1]]
results = 0

def dfs(x,y):
    if y == C-1:
        return True
    
    for dx,dy in moves:
        nx,ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C:
            if the_map[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                if dfs(nx,ny):
                    return True
        
    return False
   

for i in range(R):
    if dfs(i,0):
        results += 1

print(results)