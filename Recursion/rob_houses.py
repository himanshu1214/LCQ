class Solution:
    def rob(self, nums: List[int]) -> int:
        hash_map = {}
        def dfs(nums, index, money):
            if index> len(nums)-1:
                return money
            
            if (index, money) in hash_map:
                return hash_map[(index, money)]
            

            val = max(dfs(nums, index + 2, money + nums[index]), dfs(nums, index+1, money))
            hash_map[(index, money)] = val
            
            return val
            
        return dfs(nums, 0, 0)
        # print(hash_map)

class Solution:
    def rob(self, nums: List[int]) -> int:
        hash_map = {}
        def dfs(nums, index):
            if index> len(nums)-1:
                return 0
            
            if index in hash_map:
                return hash_map[index]
            

            val = max(dfs(nums, index + 2) + nums[index], dfs(nums, index+1))
            hash_map[index] = val
            
            return val
            
        return dfs(nums, 0)
