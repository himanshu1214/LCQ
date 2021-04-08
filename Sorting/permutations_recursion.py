def permutations(arr):
    if not arr:
        return []
    result = []
    def helper(arr, ind, slate):
        if ind >= len(slate):
            result.append(slate[:])
            return 
        else:
            for j in range(ind, len(arr)):
                arr[j], arr[ind] = arr[ind], arr[j] 
                slate.append(arr[j])
                helper(arr, ind, slate)
                slate.pop()
                arr[j], arr[ind] = arr[ind], arr[j] 

    helper(arr, 0, [])
    return result

arr =[1, 2, 3]
print(permutations(arr))