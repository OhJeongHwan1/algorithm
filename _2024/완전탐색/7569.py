# 7568 덩치 실5 완탐

import sys
input = sys.stdin.readline

N = int(input())
body = []
result_list = []

for _ in range(N):
    body.append(list(map(int,input().split())))

for i in range(N):
    result = 1
    for j in range(N):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            result += 1

    result_list.append(result)

print(*result_list)