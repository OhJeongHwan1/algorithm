# 2437 저울 골2
# 누적합의 개념에 대해 알고 숙지할 필요가 있음.

import sys

input = sys.stdin.readline

N = int(input())

weights = list(map(int,input().split()))
sums = [0 for _ in range(N)]

weights.sort()

sums[0] = weights[0]

for i in range(1,N):
    sums[i] = sums[i-1] + weights[i]

# print(weights)
# print(sums)
    
if weights[0] != 1:
    print(1)
    exit()

for i in range(N):
    if i == N-1:
        print(sums[i]+1)
        break

    if sums[i] + 1 < weights[i+1]:
        print(sums[i]+1)
        break