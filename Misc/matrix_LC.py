class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    mat[r][c] = float("inf")
                    if r > 0 and mat[r][c] > mat[r-1][c]:
                        mat[r][c] = mat[r-1][c]  + 1
                    if c > 0 and mat[r][c]> mat[r][c-1]:
                        mat[r][c] = mat[r][c-1] + 1
                        
          
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                 if mat[r][c] != 0:
                    if r < rows-1 and mat[r][c] > mat[r+1][c]:
                        mat[r][c] = mat[r+1][c]  + 1
                    if c < cols-1 and mat[r][c]> mat[r][c+1]:
                        mat[r][c] = mat[r][c+1] + 1
        
        return mat
