class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        # Logic is from bottom up
        # Knight has two ways of moving - down and right
        # For survival or entry into cell, need atleast +1 
        # From one room to another knight needs atleast health needed to reach the dest or 
        # if its too much i.e. current boost > health needed, he can just need +1 only. 
       
        dp = [[float('inf') for j in range(cols)]for i in range(rows)]
        
        def min_value(curr, row, col):
            """This method is to get min val to move to next cell based on the health needed into next                    cell
            """
            if col >= cols or row >= rows:
                return float('inf')
         
            return max(1, (dp[row][col] - curr))
            
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                curr = dungeon[r][c]
                
                right_min = min_value(curr, r, c+1)
                down_min = min_value(curr, r+1, c)
                min_val = min(right_min, down_min)
                
                if min_val != float('inf'):
                    dp[r][c] = min_val
                else:
                    dp[r][c] = 1 if curr >=0 else (1 -curr)

        return dp[0][0]
                
                
