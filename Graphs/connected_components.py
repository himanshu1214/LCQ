from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0: return n
        
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        visited =set()
        def dfs(source):
            if not graph[source]:
                return
            
            for neighbour in graph[source]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
            
        components = 0
        for src, des in edges:
            if src not in visited:
                dfs(src)
                components += 1
                
        standalonenodes = n - len(visited)
        ans = components + standalonenodes
        
        return ans
