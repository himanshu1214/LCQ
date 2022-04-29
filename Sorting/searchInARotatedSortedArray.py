class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            def find_target(nums, add_index):  
                start = 0
                end = len(nums) -1
                while start <= end:
                    mid = (start + end)//2
                    if nums[mid] == target:
                        return mid + add_index
                    elif nums[mid] > target:
                        end = mid -1
                    elif nums[mid] < target:
                        start = mid +1
                    print(mid, nums)
                return -1

            i = 0
            res = []
            while i < len(nums) - 1:
                if nums[i] > nums[i+1]:
                    print(nums[i], nums[i+1], i)
                    arr1, arr2 = nums[:i+1],  nums[i+1:]
                    break
                else:
                    arr1 = nums
                    arr2 = None
                i += 1

            start = 0
            end =  len(nums)-1
            index = i
            print(f"ARR1 {arr1}, ARR2 : {arr2},target {target}")
            
            if arr1[0] <= target and arr1[-1] >=target:

                return find_target(arr1, 0)
        
            elif arr2:
                print(arr2)
                return find_target(arr2, len(arr1))
            else:
                return -1
                


