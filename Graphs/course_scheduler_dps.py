class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        
        if not prerequisites:
            return True
        
        
        graph = collections.defaultdict(list)
        
        for node1, node2 in prerequisites:
            graph[node2].append(node1)
         
 
        path = [False]*numCourses
        checked = [False]*numCourses
        def dfs(n):
            
            if checked[n]:
                return False
            
            if path[n]:
                return True
            
            path[n] = True
            ret = False
            for nei in graph[n]:
                ret = dfs(nei)
                if ret:
                    break
                    
            path[n] = False
            
            checked[n] = True
            return ret
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
