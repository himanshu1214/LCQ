class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from queue import Queue
        rows = len(grid)
        cols = len(grid[0])

        fresh_oranges = [0]
        rotten_queue =  Queue() 
        step= 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges[0] += 1
                if grid[i][j] == 2:
                    rotten_queue.put((i, j, step))

        print(f"FRESH ORANGES outside loop : {fresh_oranges}")
        def bfs(rotten_queue):

            while not  rotten_queue.empty():
                r, c, step = rotten_queue.get()
                print("******************")
                for rw, cl in [(r, c+1), (r+1, c), (r-1, c), (r, c-1)]:
                    if (rw in range(rows)
                    and cl in range(cols) 
                    and grid[rw][cl] == 1):
                        print(f"MINS : {step} and fresh oranges {fresh_oranges[0]} and row, col : {(rw, cl)}")
                        grid[rw][cl] = 2
                        rotten_queue.put((rw, cl, step+1))
                        fresh_oranges[0] -= 1


            return step if fresh_oranges[0] == 0 else -1
        if rotten_queue.qsize() == 0 and fresh_oranges[0] == 0:
            return 0
        res = bfs(rotten_queue)
        return res
