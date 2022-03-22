class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.horz = [0]*n
        self.coln = [0]*n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int: 
        n = self.n
        move = 1
        if player == 2:
            move = -1
        self.horz[col] += move
        self.coln[row] += move
        if row == col:
            self.diag += move
        if row == n - col -1:
            self.anti_diag += move
            
        
        if abs(self.horz[col]) == n or abs(self.coln[row]) == n or abs(self.diag) == n or abs(self.anti_diag) == n:
            return player
        return 0
