class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = defaultdict(list)
        
        for i in range(len(nums)):
            hash_table[nums[i]].append(i)
            
        print(hash_table) 
        for i in nums:
            if len(hash_table[i]) > 1 and i*2 == target:
                return [hash_table[i][0], hash_table[i][1]]
            if len(hash_table[i]) == 1 and i*2 == target:
                continue
                
            if (target - i) in hash_table :
                return [hash_table[i][0], hash_table[target-i][0]]
            
            
        return []
