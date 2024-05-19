# 행렬 1080
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

origin = [list(map(int,input().strip())) for _ in range(N)]
goal = [list(map(int,input().strip())) for _ in range(N)]

if N < 3 or M < 3:
    if origin == goal:
        print(0)
    else:
        print(-1)

else:
    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            if origin[i][j] != goal[i][j]:
                cnt +=1
                for k in range(i,i+3):
                    for m in range(j,j+3):
                        origin[k][m] = 0 if origin[k][m] == 1 else 1

    if origin == goal:
        print(cnt)
    else:
        print(-1)                    
    