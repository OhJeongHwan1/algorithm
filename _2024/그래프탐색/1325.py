# 1325 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    end, start = map(int,input().split())
    adj_list[start].append(end)

def bfs(x):
    q = deque()
    q.append(start)
    cnt = 0
 
    visited = [False] * (N + 1)
    visited[start] = True
 
    while q:
        cur = q.popleft()
        for next in adj_list[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
    return cnt

result = []
for start in range(1, len(adj_list)):
    result.append(bfs(start))
    
max = max(result)
for i in range(len(result)):
    if max == result[i]:
        print(i + 1,end=' ')