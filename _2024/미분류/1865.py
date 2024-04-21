# 1865 웜홀 골3
# 벨만포드 알고리즘
import sys
input = sys.stdin.readline

TC = int(input())
INF = int(1e9)

def bellmanFord(start,vertex,edges):
    dist = [INF for _ in range(vertex+1)]

    dist[start] = 0

    for i in range(vertex):
        for j in range(len(edges)):
            curr, next, cost = edges[j]
            if dist[curr] + cost < dist[next]:
                dist[next] = dist[curr] + cost
                if i == vertex - 1:
                    return False        
    return True

for _ in range(TC):
    N, M, W = map(int,input().split())

    edges = []

    for _ in range(M):
        start, end, time = map(int,input().split())
        if start == end:
            edges.append([start,end,time])
            continue
        edges.append([start,end,time])
        edges.append([end,start,time])
    is_over = False
    for _ in range(W):
        start, end, time = map(int,input().split())
        if start == end and time > 0:
            print('YES')
            is_over = True
            break
        edges.append([start,end,-time])
    if is_over == True:
        continue
    cnt = 0
    if bellmanFord(1,N,edges) == False:
        print('YES')
    else:
        print('NO')
    