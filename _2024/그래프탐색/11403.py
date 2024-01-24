#11403 실1 경로 찾기
#인접 행렬로 주어진 그래프로 결과 만들기

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
can_go_graph = [[0 for _ in range(N)] for _ in range(N) ]

for _ in range(N):
    graph.append(list(map(int,(input().split()))))

queue = deque()

for i in range(N):
    queue.append(i)     
    visited = [False] * N
    while queue:
        next = queue.popleft()
        for k in range(N):
            if graph[next][k] == 1 and not visited[k]:
                visited[k] =True
                queue.append(k)
                can_go_graph[i][k] = 1

for list in can_go_graph:
    for can in list:
        print(can,end=' ')
    print()

