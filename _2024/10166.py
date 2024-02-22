# 10166 관중석

# import sys
# input = sys.stdin.readline

# ANGLE = 360
# D1, D2 = map(int,input().split())

# if D1 == D2:
#     print(D1)
#     exit()

# the_angles = set([])

# for num in range(D1,D2+1):
#     divide = ANGLE/num
#     for i in range(num,0,-1):
#         the_angles.add(ANGLE - divide * i)

# print(len(the_angles))

from sys import stdin
from math import gcd


def solve():
    a, b = map(int, stdin.readline().split())
    arr = [[0] * b for _ in range(b)]

    ans = 0

    for i in range(a, b + 1):
        for j in range(1, i + 1):
            g = gcd(i, j)

            x, y = i // g, j // g

            if not arr[x-1][y-1]:
                arr[x-1][y-1] = 1
                ans += 1

    print(ans)

solve()