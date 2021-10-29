class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        array = [[None for j in range(c)]for i in range(r)]
        flatten_array = [mat[i][j] for i in range(rows) for j in range(cols)]
        if r*c != rows*cols:
            return mat
        k = 0
        for i in range(r):
            for j in range(c):
                 if k < len(flatten_array):
                    array[i][j] = flatten_array[k]
                    k +=1
        return array
                
