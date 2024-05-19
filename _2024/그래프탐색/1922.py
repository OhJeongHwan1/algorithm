# 1922 네트워크 연결
import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
unions = [i for i in range(N+1)]

def find(a):
    if unions[a] != a:
        unions[a] = find(unions[a])
    return unions[a]

def union(a,b):
    unions[find(b)] = find(a)

edges = [list(map(int,input().split())) for _ in range(M)]
ans = 0
hq = []

for edge in edges:
    heapq.heappush(hq,[edge[2],edge[0],edge[1]])

while hq:
    cost, start, end = heapq.heappop(hq)

    if find(start) == find(end):
        continue

    ans += cost
    union(start,end)

print(ans)

