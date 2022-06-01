class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(row, col):
            
            if row < 0 or col < 0:
                return 0
            if row == 1 and col == 1:
                return 1
            
            if (row,col) in memo:
                return memo[(row, col)]
            
            val = 0
            val +=  helper(row-1, col)
            val += helper(row, col-1)

            memo[(row, col)] = val
            return val
        
        return helper(m, n)
