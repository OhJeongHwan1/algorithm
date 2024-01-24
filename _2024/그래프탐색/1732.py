# 1732 최단 경로
# 가중치를 포함한 인접 리스트
# 최단 거리를 구해야 하므로 다익스트라

import sys
import heapq
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())
INF = float("inf")

adj_list = [[] for _ in range(V+1)]
dist_list = [ INF for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    adj_list[u].append([v,w])

def dijkstra(start):
    queue = []
    heapq.heappush(queue,[dist_list[start],start])

    while queue:
        current_dist, current = heapq.heappop(queue)

        if dist_list[current] < current_dist:
            continue

        for next, value in adj_list[current]:
            distance = current_dist + value
            if distance < dist_list[next]:
                dist_list[next] = distance 
                heapq.heappush(queue,[distance, next])

dist_list[K] = 0
dijkstra(K)

for i in range(1,V+1):
    if dist_list[i] == INF:
        print("INF")
    else:
        print(dist_list[i])