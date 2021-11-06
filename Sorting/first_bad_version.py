# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
    

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        res = []
        while start <= end:
            
            mid = (start+end)//2
            if not isBadVersion(mid):
                start = mid+1
                
            if isBadVersion(mid):
                end = mid-1
                res.append(mid)
                
        return min(res)
        
