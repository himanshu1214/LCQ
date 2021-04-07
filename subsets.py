#Subsets problems by recursion LC: 78

def subset(arr):
    if not arr:
        return []
    result = []
    def helper(arr, ind, slate):
        if ind >= len(arr):
            result.append(slate[:])
            return 

        else:
            helper(arr, ind+1, slate)
            slate.append(arr[ind])
            helper(arr, ind+1, slate)
            slate.pop()        
    helper(arr, 0, [])
    return result

arr=[1, 2, 3]
print(subset(arr))
