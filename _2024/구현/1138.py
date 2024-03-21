# 1138 한 줄로 서기 구현 그리디

import sys
input = sys.stdin.readline

N = int(input())

line = list(map(int,input().split()))
result_list = [ 0 for _ in range(N) ]

for i in range(N):
    number = i + 1
    count = 0
    for j in range(N):
        if count == line[i] and result_list[j] == 0:
            result_list[j] = number
            break

        if result_list[j] == 0:
            count += 1


print(*result_list)

