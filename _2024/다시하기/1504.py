# 1504 특정한 최단 경로 골 4
# 그래프

import sys
input = sys.stdin.readline

N, E = map(int,input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    adj_list[a].append([b,c])
    adj_list[b].append([a,c])

v1, v2 = map(int,input().split())

print(adj_list)