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

            
