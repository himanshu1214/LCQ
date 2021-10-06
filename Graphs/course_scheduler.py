class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # given num of courses pre-req list check if we can finish all the courses
        # Condition on completing 
        # 1. Courses are in in the range of (0 to numcourses)
        # 2. Complete 1 > 0 cannot be 0 > 1 {dependencies cannot be vice-versa}
        # 3. Prerequisites be unique. 
        
        # 1.  Initially we have to create a parent child relation graph which demonstrates this relationship
        # 2. Kind of directed graph where we can move from top to bottom only
        # 3. Total number of pre-requisites are number of nodes
        # 4. Denote the relationship parent -> child as (+1) and child -> parent as (-1)
        # Base cases : 1. 
        
        #Problem : How to traverse prequisites as 
        from collections import defaultdict
        adj_list = defaultdict(list)
        
        visited  = set()
        
        for i, j in prerequisites:
            adj_list[i].append(j)
        
            
        def dfs(node):
            
            # Base case for loop
            if node in visited:
                return False
            
            # for leaf 
            if adj_list[node] == []:
                return True
             
            visited.add(node)  
            for neighbour in adj_list[node]:
                if not dfs(neighbour): return False
            visited.remove(node)
            adj_list[node] = []

            return True
        
        for crs in list(adj_list):
            if not dfs(crs): return False
        
        return True
