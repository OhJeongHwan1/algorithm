# 1197 최소 스패닝 트리 골 4
import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())

visited = [False for _ in range(V+1)]

def prim():
    visited = [False for _ in range(V+1)]
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        v1,v2,w = map(int,input().split())
        adj_list[v1].append([v2,w])
        adj_list[v2].append([v1,w])

    queue = []
    heapq.heappush(queue,[0,1])
    ans = 0

    while queue:
        weight, start = heapq.heappop(queue)
        if visited[start] == True:
            continue
        visited[start] = True
        ans += weight

        for next, cost in adj_list[start]:
            if visited[next] == False:
                heapq.heappush(queue,[cost,next])

    print(ans)


unions = [i for i in range(V+1)]

def find(a):
    if unions[a] != a:
        unions[a] = find(unions[a])
    return unions[a]

def union(a,b):
    unions[find(b)] = find(a)

def kruskal():
    adj_list = []
    for _ in range(E):
        v1,v2,w = map(int,input().split())
        adj_list.append([w,v1,v2])

    queue = []
    ans = 0
    leng = 0
    for the_list in adj_list:
        heapq.heappush(queue,the_list)
    
    while queue:
        w, v1, v2 = heapq.heappop(queue)
        
        if find(v1) == find(v2):
            continue
        ans += w
        union(v1,v2)

    print(ans)

#prim()
kruskal()