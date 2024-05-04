# 2887 행성 터널 플5
# 최소 스패닝 트리
# 정렬
import sys
import heapq
input = sys.stdin.readline

N = int(input())

planets = []
edges = []
planet_union = [ i for i in range(N+1)]

def find(a):
    if planet_union[a] != a:
        planet_union[a] = find(planet_union[a])
    return planet_union[a]

def union(a,b):
    planet_union[find(b)] = find(a)

for i in range(N):
    x, y, z = map(int,input().split())
    planets.append([x,y,z,i+1])

for i in range(3):
    planets.sort(key = lambda x: x[i])

    for j in range(N-1):
        edges.append([abs(planets[j][i]-planets[j+1][i]), planets[j][3], planets[j+1][3]])

edges.sort()
queue = []
ans = 0

for edge in edges:
    heapq.heappush(queue,edge)

while queue:
    w, v1, v2 = heapq.heappop(queue)
    
    if find(v1) == find(v2):
        continue
    ans += w
    union(v1,v2)

print(ans)