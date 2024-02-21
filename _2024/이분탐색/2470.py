# 두 용액 골5

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

liquids = list(map(int,input().split()))
the_minest = 2000000000
result = []

liquids.sort()

start = 0
end = N-1

while start != end:
    sum = liquids[start] + liquids[end]

    if abs(sum) < the_minest:
        the_minest = abs(sum)
        result = []
        result.append(liquids[start])
        result.append(liquids[end])

    if sum == 0:
        break
    if sum > 0:
        end -= 1
    if sum < 0:
        start += 1

print(*result)

