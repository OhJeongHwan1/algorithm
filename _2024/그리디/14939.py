# 14939 불끄기 플 4
# 그리디 비트마스킹
import sys
import copy
input = sys.stdin.readline

table = [list(map(str,input().strip())) for _ in range(10)]
goal = [['#' for _ in range(10)] for _ in range(10)]
MOVE = [[-1,0],[0,-1],[0,0],[1,0],[0,1]]
def solve(table,count):
    cnt = 0
    for x in range(1,10):
        for y in range(10):
            if table[x-1][y] == 'O':
                cnt += 1
                for dx,dy in MOVE:
                    nx,ny = x+dx,y+dy
                    if 0<= nx <=9 and 0<= ny <= 9:
                        table[nx][ny] = '#' if table[nx][ny] == 'O' else 'O'
                        
    if table == goal:
        return cnt + count
    else:
        return int(1e9)

ans = int(1e9)
for i in range(1 << 10):
    cp_table = copy.deepcopy(table)
    count = 0
    for j in range(10):
        if 1 << j & i != 0:
            count +=1
            for dx,dy in MOVE:
                nx,ny = dx,dy+j
                if 0<= nx <=9 and 0<= ny <= 9:
                    cp_table[nx][ny] = '#' if cp_table[nx][ny] == 'O' else 'O'

    ans = min(solve(cp_table,count),ans)

if ans == int(1e9):
    print(-1)
else:
    print(ans)



