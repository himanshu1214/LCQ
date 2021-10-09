class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        from heapq import heapify, heappush, heappop
        from queue import Queue

        visited =  set()

        min_heap = []
        cost_list = [0]

        def bfs(city, val):
            cost = 0
            heappush(min_heap, (val, city))
            while len(visited) < n and min_heap:
                val, city = heappop(min_heap)
            # Visited all cities:
                if city not in visited:
                    visited.add(city)
                    cost += val

                    for destinations, tr_cost in city_map[city]:
                        heappush(min_heap, (tr_cost, destinations))


            cost_list[0] = cost
            print(cost_list)
            return


        city_map = defaultdict(list)
        for city, destination, cost in connections:
            city_map[city].append((destination, cost))
            city_map[destination].append((city, cost))

        connected_components = 0
        for city in list(city_map):
            if city not in visited:
                bfs(city, 0)
                connected_components += 1
            if connected_components > 1 or len(visited) < n:
                return -1

        return cost_list[0]
