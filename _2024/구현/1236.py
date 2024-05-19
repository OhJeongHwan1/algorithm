# 1236 성지키기 브1
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
floor = [list(map(str,input().strip())) for _ in range(N)]
need_columns = []
ans = 0

for y in range(M):
    cnt = 0
    for x in range(N):
        if floor[x][y] == 'X':
            cnt += 1
    if cnt == 0:
        need_columns.append(y)

need_columns = set(need_columns)

for x in range(N):
    if x == N-1:
            for y in range(M):
                if y in need_columns:
                    need_columns.remove(y)
                    floor[x][y] = 'X'
                    ans += 1
    if 'X' not in floor[x]:
        cnt = 0
        for y in range(M):
            if y in need_columns:
                need_columns.remove(y)
                floor[x][y] = 'X'
                ans += 1
                cnt += 1
                break
        if cnt == 0:
            floor[x][M-1] = 'X'
            ans += 1
print(ans)