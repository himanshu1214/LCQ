class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: [] for i in range(9)}
        col = {c: [] for c in range(9)}
        box = {b: [] for b in range(9)}
        
        rows = len(board)
        cols = len(board[0])
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    if board[r][c] not in row[r]:
                        row[r].append(board[r][c])
                    else:
                        return False
                    if board[r][c] not in col[c]:
                        col[c].append(board[r][c])
                    else:
                        return False
                    
                    if board[r][c] not in box[r//3*3+ c//3]:
                        box[r//3*3+c//3].append(board[r][c])
                    else:
                        return False
        return True
                    
