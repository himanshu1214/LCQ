#BFS
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        col, row = len(grid[0]), len(grid)
        q = Queue()
        visited = set()
        n_islands = 0  
       

        def bfs(r, c):
            q.put((r, c))
            visited.add((r, c))
            while not q.empty():
                r1, c1 = q.get()
                for dr, dc in neighbours:
                    rw =  r1 + dr
                    cl = c1 + dc
                    if (rw in range(len(grid)) and 
                    cl in range(len(grid[0])) and 
                    grid[rw][cl] == "1" and
                    (rw,  cl) not in visited):
                        q.put((rw, cl))
                        visited.add((rw, cl))
                        
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    n_islands += 1
        return n_islands
                
# DFS           
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        def dfs(r, c):
            if (r, c) in visited:
                return 
            
            visited.add((r, c))
            for rw, cl in [(r, c-1), (r+1, c), (r-1, c), (r, c+1)]:
                if rw in range(rows) and cl in range(cols) and grid[r][c] == "1":
                    dfs(rw, cl)
                    
        islands_count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] != "0":
                    islands_count += 1
                    dfs(r, c)

        return islands_count
