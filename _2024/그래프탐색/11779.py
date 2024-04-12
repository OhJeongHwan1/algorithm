# 1504 특정한 최단 경로 골 4
# 그래프

import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float("inf")
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    adj_list[a].append([b,c])

START, END = map(int,input().split())

def dijkstra():
    queue = []
    dist = [ INF for _ in range(n+1)]
    before = [ -1 for _ in range(n+1)]

    heapq.heappush(queue,[0,START])

    dist[START] = 0

    while queue:
        weight, start = heapq.heappop(queue)
        if dist[start] < weight:
            continue

        for end, w in adj_list[start]:
            if dist[end] > weight + w:
                heapq.heappush(queue,[weight + w,end])
                dist[end] = weight + w
                before[end] = start

    print(dist[END])

    path = [END]
    now = END

    while now != START:
        now = before[now]
        path.append(now)

    print(len(path))
    list.reverse(path)
    print(*path)

dijkstra()