# 11660 구간 합 구하기 
# 동적 프로그래밍

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

the_map = [list(map(int,input().split())) for _ in range(N)]
dp_map = [[ 0 for _ in range(N+1) ] for _ in range(N+1) ]
the_area = [list(map(int,input().split())) for _ in range(M)]
results = []

for i in range(1,N+1):
    for j in range(1,N+1):
        dp_map[i][j] = dp_map[i][j-1] + dp_map[i-1][j] - dp_map[i-1][j-1] + the_map[i-1][j-1]

for x1,y1,x2,y2 in the_area:
    
    sum = dp_map[x2][y2] - dp_map[x2][y1-1] -dp_map[x1-1][y2] + dp_map[x1-1][y1-1]

    results.append(sum)

for result in results:
    print(result)

