# 17182 우주 탐사선
# 그래프
# 비트 마스킹
# queue 를 사용하는 방식은 숫자가 커지는 경우 기하 급수적으로 증가할 수 있기에
# 플로이드 워샬을 사용해야 함.
# 졌잘싸

# import sys
# from collections import deque
# input = sys.stdin.readline

# INF = float('inf')
# N, K = map(int,input().split())
# the_map = [list(map(int,input().split())) for _ in range(N)]
# all_bit = (1 << N) - 1
# queue = deque()
# queue.append([K, (1 <<K) & all_bit,0])
# ans = INF

# while queue:
#     now, visited, dist = queue.popleft()

#     if visited == all_bit and dist < ans:
#         ans = dist
#         continue
#     if dist > ans:
#         continue

#     for j in range(N):
#         if the_map[now][j] != 0 and dist + the_map[now][j] < ans:
#             add = (1 << j & all_bit)
#             queue.append([j,visited | add, dist + the_map[now][j]])

# if ans == INF:
#     print(0)
# else:
#     print(ans)

def floyd_warshall(dist, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def solve(N, K, dist):
    floyd_warshall(dist, N)
    dp = [[float('inf')] * N for _ in range(1 << N)]
    dp[1 << K][K] = 0

    for mask in range(1 << N):
        for u in range(N):
            if not (mask & (1 << u)):
                continue
            for v in range(N):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    return min(dp[(1 << N) - 1][i] for i in range(N))

# 입력
N, K = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(solve(N, K, dist))
