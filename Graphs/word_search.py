class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        
        visited = set()
        def dfs(r, c, index):
            if index > len(word)-1:
                return True
            
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != word[index]:
                return False
            
            board[r][c] = "#"
            for _r, _c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                ret = dfs(_r, _c, index+1)
                if ret:
                    break
                
            board[r][c] = word[index]
            
            return ret
        
        for rw in range(rows):
            for cl in range(cols):
                if dfs(rw, cl, 0):
                    return True
        return False
