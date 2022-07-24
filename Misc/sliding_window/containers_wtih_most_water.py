class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = float('-inf')
        
        start, end = 0, len(height)-1
        while start <= end:
            print(start, end)
            width = end - start
            calc = min(height[start], height[end])*width
            
            if calc > max_val:
                max_val = calc
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_val
