# 2961 도영이가 만든 맛있는 음식
# 비트 마스킹
# 실 2

import sys

input = sys.stdin.readline

N = int(input())
foods = []
MAX = 1e9
ans = MAX

for _ in range(N):
    foods.append(list(map(int,input().split())))

for set in range(1,1 << N):
    s = 1
    b = 0

    for j in range(N):
        if (set & (1 << j)) == (1 << j):
            s *= foods[j][0]
            b += foods[j][1]

    ans = min(ans,abs(s-b))

print(ans)

        

    