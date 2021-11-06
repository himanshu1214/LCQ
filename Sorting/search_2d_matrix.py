class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        rows = len(matrix)
        cols = len(matrix[0])
        mat_list = [matrix[r][c] for r in range(rows) for c in range(cols)]
        if len(mat_list) == 0:
            return False
        
        start, end = 0,  len(mat_list)-1
        
        if len(mat_list) == 1:
            if target == mat_list[0]:
                return True
            
        while start <= end:
            mid = (start+end)//2 
            
            if target < mat_list[mid]:
                end = mid-1
            elif target > mat_list[mid]:
                start = mid+1
            elif target == mat_list[mid]:
                return True

        return False




