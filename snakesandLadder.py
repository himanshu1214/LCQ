class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)
        
        def convertRowColToNum(num):
            r = (num - 1) // n
            c = (num-1) % n
            if r % 2:  # even
                c = n- c -1
            return [r, c]
            
        from queue import Queue
        q = Queue()
        q.put([1, 0])
        
        visit = set()
        while not q.empty():
            num, moves = q.get()
            for i in range(1, 7):
                nextnum = num + i

                
                r, c = convertRowColToNum(nextnum)
                if board[r][c] != -1:
                    nextnum = board[r][c]

                if nextnum == n*n:
                    return moves + 1

                if (r, c) not in visit:
                    visit.add((r, c))
                    q.put([nextnum, moves + 1])

        return -1
