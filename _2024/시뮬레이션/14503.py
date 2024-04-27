# 로봇 청소기 골5
# 시뮬레이션

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
r, c, d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
x = r
y = c

def change_direction(dx,dy):
    if dx == -1 and dy == 0:
        return 0
    if dx == 0 and dy == -1:
        return 3
    if dx == 1 and dy == 0:
        return 2
    if dx == 0 and dy == 1:
        return 1
ans = 0
while True:
    if room[x][y] == 0:
        room[x][y] = -1
        ans += 1
    if d == 0:
        cnt = 0
        for dx, dy in [[0,-1],[1,0],[0,1],[-1,0]]:
            nx,ny = x+dx,y+dy
            if room[nx][ny] == 0:
                cnt += 1
                x,y = nx,ny
                d = change_direction(dx,dy)
                break
        if cnt == 0:
            if room[x+1][y] == 1:
                break
            else:
                x = x+1
    elif d == 3:
        cnt = 0
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny = x+dx,y+dy
            if room[nx][ny] == 0:
                cnt += 1
                x,y = nx,ny
                d = change_direction(dx,dy)
                break
        if cnt == 0:
            if room[x][y+1] == 1:
                break
            else:
                y = y+1
    elif d == 2:
        cnt = 0
        for dx, dy in [[0,1],[-1,0],[0,-1],[1,0]]:
            nx,ny = x+dx,y+dy
            if room[nx][ny] == 0:
                cnt += 1
                x,y = nx,ny
                d = change_direction(dx,dy)
                break
        if cnt == 0:
            if room[x-1][y] == 1:
                break
            else:
                x = x-1
    elif d == 1:
        cnt = 0
        for dx, dy in [[-1,0],[0,-1],[1,0],[0,1]]:
            nx,ny = x+dx,y+dy
            if room[nx][ny] == 0:
                cnt += 1
                x,y = nx,ny
                d = change_direction(dx,dy)
                break
        if cnt == 0:
            if room[x][y-1] == 1:
                break
            else:
                y = y-1
    
print(ans)
