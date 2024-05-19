# 1546 브 1 평균

import sys
input = sys.stdin.readline
N = int(input())
scores = list(map(int,input().split()))
high = max(scores)

sum = 0

for score in scores:
    sum += score/high * 100

print(sum/N)