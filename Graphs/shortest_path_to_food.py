from queue import Queue
from collections import defaultdict
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        col = len(grid[0])
        row = len(grid)
        visited = set()
        node_distance = defaultdict(int)
        q = Queue()
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = [0]
        def bfs(r, c):
            col = len(grid[0])
            row = len(grid)
            q.put((r, c))
            visited.add((r, c))
            node_distance[(r,c)] = 0
            while not q.empty():
                r, c = q.get()
                for dr, dc in neighbours:
                    rw, cl = r + dr, c+dc
                    if (rw in range(row) and 
                       cl in range(col) and
                       (rw, cl) not in visited
                       and grid[rw][cl] != "X"):
                        q.put((rw, cl))
                        node_distance[(rw, cl)] = node_distance[(r, c)] + 1
                        visited.add((rw, cl))
                        if grid[rw][cl] == "#":
                            result[0] = node_distance[(rw, cl)]
                            return
            result[0] = -1
            return
                        
 
                    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "*":
                    bfs(r, c) # row and col to reach 
                    break
                    
                
        
        return result[0]
        
