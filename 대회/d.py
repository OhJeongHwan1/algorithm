from collections import defaultdict, deque
import sys

input = sys.stdin.readline

class Solution:
    def numBusesToDestination(self, routes, S, T):
        # 각 정류장을 지나는 노선들
        to_route = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                to_route[stop].add(i)

        # BFS 탐색
        bfs = deque([(S, 0)])
        seen_stops = {S} # 방문한 정류장
        seen_routes = set() # 방문한 노선

        while bfs:
            stop, buses = bfs.popleft()
            if stop == T:
                return buses
            for route_i in to_route[stop]:
                if route_i in seen_routes: # 해당 노선을 이미 확인했으면 skip
                    continue
                for next_stop in routes[route_i]:
                    if next_stop not in seen_stops:
                        seen_stops.add(next_stop)
                        bfs.append((next_stop, buses + 1))
                seen_routes.add(route_i) # 해당 노선 확인 표시

        return -77

if __name__ == "__main__":
    sol = Solution()
    T = int(input().strip())
    results = []
    for _ in range(T):
        B = int(input().strip())
        routes = []
        for _ in range(B):
            A = int(input().strip())
            route = list(map(int, input().split()))
            routes.append(route)
        S = int(input().strip())
        D = int(input().strip())
        result = sol.numBusesToDestination(routes, S, D)
        results.append(result)

    for r in results:
        print(r)
