class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from queue import Queue
        q =  Queue()
        global visited
        def bfs(q, row, col):
            neighbour_list = [(1, 0), 
                  (-1, 0), 
                 (0, -1), 
                 (0, 1)]
            is_ln = 1
            q.put((row, col))
            visited.add((row, col))
            while not q.empty():
                _rw, _cl = q.get()
                for r, c in neighbour_list:
                    rw, cl = _rw + r, _cl + c
                    if (rw in range(len(grid))
                       and cl in range(len(grid[0]))
                       and (rw, cl) not in visited
                       and grid[rw][cl] == 1):
                        visited.add((rw, cl))
                        q.put((rw, cl))
                        is_ln += 1
            return is_ln
        

        visited = set()
        island_length = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1
                   and (i, j) not in  visited):
                    tmp = bfs (q, i, j)
                    print(tmp, len(visited))
                    if tmp > island_length:
                        island_length = tmp


        return island_length
