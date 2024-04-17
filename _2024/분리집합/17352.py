# 17352 여러분의 다리가 되어 드리겠습니다!
# 골 5 분리집합

import sys
input = sys.stdin.readline

N = int(input())
bridge = []
island = [i for i in range(N+1)]

def find(a):
    if island[a] != a:
        island[a] = find(island[a])
    return island[a]

def union(a,b):
    island[find(b)] = find(a)

for _ in range(N-2):
    bridge.append(list(map(int,input().split())))

for brid in bridge:
    if brid[0] > brid[1]:
        union(brid[1],brid[0])
    else:
        union(brid[0],brid[1])

result = []

for i in range(1,N+1):
    if island[i] == i:
        result.append(i)

print(*result)