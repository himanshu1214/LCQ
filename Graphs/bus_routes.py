class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Navigate from source stop to target stop
        # Create Graph using stop as nodes and routes as edges
        # Use BFS to move from around edges(routes)
        from collections import defaultdict
        from queue import Queue
        S, T = source, target
        graph = defaultdict(set)

        for route, _stop in enumerate(routes):
            for k in _stop :
                graph[k].add(route)

        q = Queue()
        q.put((S, 0))
        bus_ct = 0
        seen = set()
        while not q.empty():
            stop, bus = q.get()
            if T == stop: return bus
            for route in graph[stop]:
                for st in routes[route]:
                    if st not in seen:
                        seen.add(st)
                        q.put((st, bus+1))
                routes[route] = []
                        
        return -1
