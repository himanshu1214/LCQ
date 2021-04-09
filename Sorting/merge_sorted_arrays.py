class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = 0
        while ind <= n-1:
            nums1[m+ind] = nums2[ind]
            ind+=1
        nums1.sort()
