# N과M (2) 실3

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int,input().split())

for list in combinations([i+1 for i in range(N)],M):
    print(*list)

