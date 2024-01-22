# 아주 정석적인 bfs, dfs

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

# 인접 리스트 초기화
adj_list = [[] for _ in range(N + 1)]

# 간선 정보 입력받아 인접 리스트에 추가
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 인접 리스트 내부 정렬
for edges in adj_list:
    edges.sort()

# DFS 구현
def depth(current):
    if visited[current]:
        return
    visited[current] = True
    dfs.append(current)
    for next in adj_list[current]:
        if not visited[next]:
            depth(next)

visited = [False for _ in range(N + 1)]
dfs = []

depth(V)

# 결과 출력
if dfs:
    print(*dfs)
else:
    print(V)

# BFS 구현
visited = [False for _ in range(N + 1)]
queue = deque([V])
bfs = []

while queue:
    current = queue.popleft()
    if not visited[current]:
        visited[current] = True
        bfs.append(current)
        for next in adj_list[current]:
            if not visited[next]:
                queue.append(next)

# 결과 출력
print(*bfs)
