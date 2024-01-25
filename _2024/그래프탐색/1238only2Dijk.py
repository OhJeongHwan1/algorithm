import sys
import heapq

input = sys.stdin.readline
INF = float("inf")
N, M, X = map(int, input().split())

# 정방향 그래프와 역방향 그래프 초기화
forward_adj_list = [[] for _ in range(N + 1)]
backward_adj_list = [[] for _ in range(N + 1)]

# 간선 정보를 두 그래프에 각각 저장
for _ in range(M):
    u, v, w = map(int, input().split())
    forward_adj_list[u].append([v, w])
    backward_adj_list[v].append([u, w])

# 다익스트라 알고리즘
def dijkstra(start, adj_list):
    distances = [INF for _ in range(N + 1)]
    queue = []
    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current = heapq.heappop(queue)
        if current_distance > distances[current]:
            continue

        for next, distance in adj_list[current]:
            next_distance = distance + current_distance
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(queue, [next_distance, next])

    return distances

# 정방향과 역방향에 대해 각각 다익스트라 알고리즘 실행
distances_to_X = dijkstra(X, backward_adj_list)
distances_from_X = dijkstra(X, forward_adj_list)

# 최대 거리 계산
max_distance = 0
for i in range(1, N + 1):
    distance = distances_to_X[i] + distances_from_X[i]
    if distance > max_distance:
        max_distance = distance

print(max_distance)
