#1260 bfs dfs 그래프를 만들어주지 않고 배열로만

import sys
from collections import deque

input=sys.stdin.readline

N, M, V = map(int,(input().split()))

vertex = []
visited = [ False for _ in range(N+1)]

dfs = []

for i in range(M):
    vertex.append(list(map(int,(input().split()))))

for list in vertex:
    list.sort()

vertex.sort()

def depth(current):
    if visited[current] == True:
        return
    
    visited[current] = True
    dfs.append(current)

    for start,end in vertex:
        if start == current:
            depth(end)
        if end == current:
            depth(start)
        


for start,end in vertex:
    if start == V:
        depth(start)
    if end == V:
        depth(end)

if len(dfs) != 0:
    for vert in dfs:
        print(vert,end=' ')
else:
    print(V,end="")

visited = [ False for _ in range(N+1)]
queue = deque()
bfs = []

queue.append(V)

while len(queue) > 0:
    current = queue.popleft()

    bfs.append(current)
    visited[current] = True
    
    for start, end in vertex:
        if start == current:
            if visited[end] != True:
                queue.append(end)
                visited[end] = True
        if end == current:
            if visited[start] != True:
                queue.append(start)
                visited[start] = True

print()
for vert in bfs:
    print(vert,end=' ')
