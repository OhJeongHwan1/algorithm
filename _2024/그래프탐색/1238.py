# 1238 파티 
# 다익스트라를 n 번 사용하여 각각 노드에 대하여 실행함
# 하지만 최적의 방법은 정방향 간선과 역방향 간선으로 만들어서 각각에 대하여 실행
# 오직 2번의 다익스트라로도 해결할 수 있다.
import sys
import heapq

input = sys.stdin.readline
INF = float("inf")
N,M,X = map(int,input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int,input().split())
    adj_list[u].append([v,w])

def dijkstra(start):
    come_back_distance = [ INF for _ in range(N+1)]
    queue = []
    come_back_distance[start] = 0
    heapq.heappush(queue,[come_back_distance[start],start])

    while queue:
        current_distance, current = heapq.heappop(queue)
        if current_distance > come_back_distance[current]:
            continue

        for next, distance in adj_list[current]:
            next_distance = distance + current_distance
            if next_distance < come_back_distance[next]:
                come_back_distance[next] = next_distance
                heapq.heappush(queue,[next_distance,next])

    return come_back_distance

result_list = dijkstra(X)
result_list[0] = 0


for i in range(1,N+1):
    if X==i:
        continue
    for_result = dijkstra(i)
    result_list[i] += for_result[X]

print(max(result_list))