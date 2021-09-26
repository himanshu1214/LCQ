class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def helper(rw, cl, index):
            if index == len(word):
                return True

            if (rw not in range(len(board))
            or cl not in range(len(board[0]))
            or (rw, cl) in visited 
            or board[rw][cl] != word[index]):
                return False
            
            visited.add((rw, cl))
            res =  (helper(rw+1, cl, index +1) or 
                    helper(rw-1, cl, index+1) or 
                    helper(rw, cl+1, index+1) or 
                    helper(rw, cl-1, index+1))
            visited.remove((rw,cl))
            return res


        row, col  = len(board), len(board[0])
        visited = set()
        for i in range(row):
            for j in range(col):
                if  helper(i, j, 0):
                    return True
        return False

      # Typical Graph DFS question
      # O(4^n)
