# 1931 회의실
# 그리디와 우선순위 큐 사용
# 끝나는 시간이 빠른 시간들 선택

import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = []
shortest_list = []

for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(queue, [b, a])

shortest_list.append(heapq.heappop(queue))

while queue:
    end_time, start_time = heapq.heappop(queue)
    
    if start_time >= shortest_list[-1][0]:
        shortest_list.append([end_time,start_time])

print(len(shortest_list))

