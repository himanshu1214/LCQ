class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid == None or len(grid) == 0:
            return 0
        
        def dfs(grid, row, col):
            
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0  or grid[row][col] != '1':
                return 


            grid[row][col] = 0
            dfs(grid, row+1, col)
            dfs(grid, row, col+1)
            dfs(grid, row-1, col)
            dfs(grid, row, col-1)
            
        ct = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ct += 1
                    dfs(grid, r, c)

                    
        return ct
   
# Alternate
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        
        visited = set()
        def dfs(rw, cl):
            if (rw, cl) in visited:
                return 
            
            visited.add((rw, cl))
            for ro, co in [(rw+1, cl), (rw-1, cl), (rw, cl+1), (rw, cl-1)]:
                    if ro in range(rows) and co in range(cols) and grid[ro][co] == "1":
                        dfs(ro, co)
            
            
            
        count = 0 
        for _r in range(rows):
            for _c in range(cols):
                if (_r, _c) not in visited and grid[_r][_c] == '1' :
                    count += 1
                    dfs(_r, _c)
        return count
            
