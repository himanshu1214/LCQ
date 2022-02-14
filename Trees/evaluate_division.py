class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # eq: [["a", "b], ["b", "c"]] = [2.0, 3.0]
        # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        
        # a ====>(2.0) b ===> c(3.0) => a ====> c ?? = 6
        # we can draw bi - direction map which provides the relationship
        # Every string is a node, and edge between two nodes is value
        # Every query to exist so both nodes should exist in graph
        # Two condition 1. If not exist --> 1. return -1
         #              2. If exists (i.e. both nodes exis) traverse using depth first  and reach. else -1
        from collections import defaultdict
        graph = defaultdict(defaultdict)
        # create graph
        for eq, val in zip(equations, values):
            graph[eq[0]][eq[1]] = val
            graph[eq[1]][eq[0]] = 1/val
            
        
        def dfs(num, den,cal, visited):
            visited.add(num)
            ret = -1.0
            neighbours = graph[num]
            if den in neighbours:
                ret = cal*neighbours[den]
            else:
                for neighbour, val in neighbours.items():
                    if neighbour not in visited:
                        ret = dfs(neighbour, den, cal*val, visited)

                    if ret != -1.0:
                        break
            visited.remove(num)
            return ret    
                    
            
        res = []
        visited = set()
        for fir, sec in queries:
            
                  
            if fir not in graph or sec not in graph:
                  ret = -1.0
                    
            elif fir == sec:
                ret = 1.0
            else:
            
                # find a path from dividend to divisor using DFS/backtracking
                ret = dfs(fir, sec, 1, visited)
            res.append(ret)
                    
        return res
