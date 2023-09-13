import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
n = 0
while True:
    n+=1
    try:
        N = int(input())
        distance = [[INF for _ in range(N)] for _ in range(N)]
        graph = []
        if N >= 2:
            for i in range(N):
                buf = list(map(int, input().split()))
                graph.append(buf)
            def dijkstra():
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                q = []
                heapq.heappush(q, [0, 0])

                distance[0][0] = graph[0][0]
                while q:
                    y, x = heapq.heappop(q)
                    if distance[y][x] < graph[y][x]:
                        continue

                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]

                        if 0 <= ny < N and 0 <= nx < N:
                            if distance[ny][nx] > distance[y][x] + graph[ny][nx]:
                                distance[ny][nx] = distance[y][x] + graph[ny][nx]
                                q.append([ny,nx])
            dijkstra()
            print("Problem {}: {}".format(n, distance[N-1][N-1]))
        else:
            break
    except:
        break