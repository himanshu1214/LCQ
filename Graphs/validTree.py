class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge less than n-1 means its not fully connected 
        # edges more than n-1 means the graph contains cycle
        
        if len(edges) != n - 1: return False
        
        graph =[[] for _ in range(n)]
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
 
        dfs(0)
        return len(visited) == n
    
                
