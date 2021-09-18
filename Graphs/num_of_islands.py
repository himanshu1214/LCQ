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
                
            
