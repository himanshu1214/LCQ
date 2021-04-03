# Complete the function below.

def findZeroSum(arr):
    # Write your code here.
    def helper2_sum(arr, ind_3, target):
        start = 0
        end = len(arr)-1 
        arr[ind_3], arr[start] = arr[start], arr[ind_3]
        start +=1
        while start <= end:
            if arr[start] + arr[end] > target:
                end -=1
            elif arr[start] + arr[end] < target:
                start += 1
            else:
               nums = [arr[start], arr[end], arr[0]]
               nums.sort()
               return (', '.join((str(nums[0]), str(nums[1]), str(nums[2]))))
        return   
    result = []
    for i in range(len(arr)-1):
        target = 0-arr[i]
        tmp = helper2_sum(arr, i, target)
        if tmp:
            if tmp not in result:
                result.append(tmp)
    return result
