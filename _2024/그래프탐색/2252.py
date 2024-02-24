# 2252 줄세우기
# 신유형임 익힐 필요 있음.
# 위상 정렬 문제임.

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
statures = [ list(map(int,input().split())) for _ in range(M) ]
adj_list = [[] for _ in range(N+1)]
inDegree = [ 0 for _ in range(N+1)]
queue = deque()
result_list = []

for sm, big in statures:
    adj_list[sm].append(big)
    inDegree[big] += 1

for i in range(1,N+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    start = queue.popleft()
    result_list.append(start)

    for end in adj_list[start]:
        inDegree[end] -= 1
        if inDegree[end] == 0:
            queue.append(end)
            

print(*result_list)
