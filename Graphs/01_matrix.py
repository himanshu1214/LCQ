from queue import Queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = Queue()
        visited = set()
        
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.put((r, c))
                    visited.add((r, c))
        
        
        def bfs():       
            while not q.empty():
                rw, cl = q.get()
                
                for _r, _c in [(rw + 1, cl),  (rw, cl + 1),(rw,  cl-1), (rw - 1,  cl)]:
                    if _r in range(rows) and _c in range(cols) and (_r, _c) not in visited:
                        visited.add((_r, _c))
                        q.put((_r, _c))
                        mat[_r][_c] = mat[rw][cl] + 1
            return mat
        
        return bfs()
