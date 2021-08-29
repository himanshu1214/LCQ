class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        result = []
        if not nums:
            if lower == upper:
                result.append(str(lower))
                return result
            val =  str(lower) + '->' + str(upper)  if upper - lower > 2 else str(lower +1) 
            result.append(val)
                    
        if len(nums) == 1:
            if upper - nums[0] >= 1:
                val =  str(nums[0]+1)  + '->' + str(upper)
                result.append(val)
                return result
            elif nums[0] -lower >=1:
                val =   str(lower)  + '->' + str(nums[0]-1) 
                result.append(val)
                return result
            else:
                return []



        if len(nums) == 2:
            if nums[1] - nums[0] > 0:
                val =  val = str(nums[0]+1) + '->' + str(nums[1]-1) if nums[1] - nums[0] > 2 else str(nums[1] -1) 
                result.append(val)
            return result
        
        start =0 

        while start < len(nums):
            val = ""

            if start > 0 and start < len(nums)-1:
                if nums[start] == 603977020:
                    print(f"Checkfor this : {nums[start]}")
                if nums[start+1]- nums[start]> 1:
                    val = str(nums[start]+1) + '->' + str(nums[start+1]-1) if nums[start+1] - nums[start] > 2 else str(nums[start] +1) 
                    result.append(val)
                if upper - nums[-1] >= 1 and start == len(nums)-2:
                    val = str(nums[-1] +1) + '->' + str(upper) if upper - nums[-1] > 2 else str(nums[-1] +1) 
                    result.append(val) 

            if  start== 0 :
                if nums[0] - lower >=  1:
                    val = str(lower) + '->' + str(nums[0]-1) if lower - nums[0] < -2 else str(nums[0] -1) 
                    result.append(val)

                if nums[1]-nums[0]>1:
                    val = str(nums[0]+1) + '->' + str(nums[1]-1) if nums[1] - nums[0] > 2 else str(nums[1] -1)
                    result.append(val)

            start += 1
            print(val)

        return result


