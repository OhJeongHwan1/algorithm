# 5062 전화번호 목록 골4
# 정렬

import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    numbers = [input().strip() for _ in range(N)]
    numbers.sort()

    no = False
    for i in range(N-1):
        if len(numbers[i]) < len(numbers[i+1]):
            cnt = 0
            for j in range(len(numbers[i])):
                if numbers[i][j] != numbers[i+1][j]:
                    break
                else:
                    cnt+=1

            if cnt == len(numbers[i]):
                no = True

    if no == True:
        print("NO")
    else:
        print("YES")

