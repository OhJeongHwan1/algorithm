from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, S, T):
        # 각 정류장을 지나는 노선들
        to_route = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                to_route[stop].add(i)

        # 노선들 간의 연결 관계를 나타내는 그래프
        graph = defaultdict(set)
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                # 두 노선이 하나 이상의 정류장을 공유할 경우
                if any(stop in routes[j] for stop in routes[i]):
                    graph[i].add(j)
                    graph[j].add(i)

        bfs = deque([(S, 0)])
        seen_stops = {S}
        seen_routes = set()

        while bfs:
            stop, buses = bfs.popleft()
            if stop == T:
                return buses
            for route_i in to_route[stop]:
                if route_i in seen_routes:
                    continue
                seen_routes.add(route_i)
                for next_stop in routes[route_i]:
                    if next_stop not in seen_stops:
                        seen_stops.add(next_stop)
                        bfs.append((next_stop, buses + 1))
                for next_route in graph[route_i]:
                    if next_route not in seen_routes:
                        seen_routes.add(next_route)  # 추가된 부분
                        for next_stop in routes[next_route]:
                            if next_stop not in seen_stops:
                                seen_stops.add(next_stop)
                                bfs.append((next_stop, buses + 1))
        
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
