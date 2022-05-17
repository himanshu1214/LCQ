class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        prefix = [1]
        postfix = []
        res = []
        for i in range(len(nums)-1):
            pre = pre*nums[i]
            prefix.append(pre)
            
        for j in range(len(nums)-1, 0, -1):
            post = post*nums[j]
            postfix.append(post)
        postfix.reverse()
        postfix.append(1)

        

        for k in range(len(nums)):
            res.append(postfix[k]*prefix[k])

        return res
