class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row, col = [0]*3, [0]*3
        diag, anti_diag = 0, 0
        
        player = 1
        for chance, rc in zip(range(9), moves):
            r, c = rc[0], rc[1]
            if chance % 2:
                player = -1
            else:
                player = 1
            
            print(chance)
            row[c] += player
            col[r] += player
            if r == c:
                diag += player
            if r == 3 - c -1:
                anti_diag += player
            
            if abs(row[c]) == 3 or abs(col[r]) == 3 or abs(diag) == 3 or abs(anti_diag) == 3:
                return 'A' if player == 1 else 'B'
            
        return "Draw" if chance == 8 else "Pending"
