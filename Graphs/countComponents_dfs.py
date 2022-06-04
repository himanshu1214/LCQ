class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        import collections
        graph = [[] for i in range(n)]
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        
        def dfs(n):
            
            if n in visited:
                return 
            
            visited.add(n)
            for nei in graph[n]:
                dfs(nei)
            
        ct = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ct += 1
                
        return ct
