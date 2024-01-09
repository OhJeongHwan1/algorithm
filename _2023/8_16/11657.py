import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))

def bellman_ford(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    for i in range(n):
        for (start, end, cost) in edges:
            if distance[start] != float('inf') and distance[start] + cost < distance[end]:
                distance[end] = distance[start] + cost
                
                if i == n - 1:
                    return -1
    return distance

result = bellman_ford(1)

if result == -1:
    print("-1")
else:
    for i in range(2, n+1):
        print(result[i] if result[i] != float('inf') else "-1")