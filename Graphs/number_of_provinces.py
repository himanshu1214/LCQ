class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict
        visited = set()
        city_graph = defaultdict(list)
        rows = len(isConnected)
        cols = len(isConnected[0])
        for r in range(rows):
            for c in range(r+1, cols):
                if isConnected[r][c] == 1:
                    city_graph[r].append(c)
                    city_graph[c].append(r)
                    
                    
        
        def dfs(city):
            if not city_graph[city]:
                return 
            
            for neighbour in city_graph[city]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
                
        provinces = 0
        for city in range(rows):
            if city not in visited:
                dfs(city)
                provinces += 1
                    
        return provinces
