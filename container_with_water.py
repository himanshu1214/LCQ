class Solution:
    def maxArea(self, height: List[int]) -> int:
        lstart = 0
        rstart = len(height) - 1
        max_area = 0
        while lstart < len(height) and rstart >=0:
            xdist = rstart - lstart
            ydist = min(height[lstart], height[rstart])
            t_max_area = xdist*ydist
            if t_max_area > max_area:
                max_area = t_max_area
            if height[lstart] < height[rstart]:
                lstart += 1
            else:
                rstart -= 1
        return max_area

  
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_area = 0
        while start <= end:
            
            tmp_area = min(height[start], height[end])*(end - start)
            if tmp_area > max_area:
                max_area = tmp_area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area
