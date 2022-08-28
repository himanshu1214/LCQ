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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lft, rht = [1 for i in range(len(nums))], [1 for i in range(len(nums))]
        res = []
        for i in range(1, len(nums)):
            lft[i] = lft[i-1]*nums[i-1]
            
        for j in range(len(nums)-2, -1, -1):
            rht[j] = rht[j + 1] * nums[j+1]
            
        for k in range(len(nums)):
            res.append(lft[k]*rht[k])
            
        return res
        
