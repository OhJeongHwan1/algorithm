import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    que = []
    heapq.heappush(que, (0, start))
    
    while que:
        cost, current = heapq.heappop(que)
        if distance[current] < cost:
            continue
        
        for next_node, next_cost in graph[current]:
            total_cost = cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(que, (total_cost, next_node))
                
    return distance

result = dijkstra(start)
print(result[end])

