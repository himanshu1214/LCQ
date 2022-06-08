class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find a cell which can pass water to both pacific and atlantic
        # condition: prev_cell < cell
        # we use dfs along the border of Pacific and Atlantic
        # Find the visited cells for Pacific and Atlantic
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited 
                or  r == rows or r < 0
                or c == cols or c < 0
                or prev_height > heights[r][c]):
                return

            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
                
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows -1, c, atl, heights[rows-1][c])
            
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
            
        final_list = []
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    final_list.append([r, c])
                    
        return final_list
