def mergeArrays(arr):
    #
    # Write your code here.
    #
    k = len(arr)
    n = len(arr[0])
    
    asc= False
    for i in range(k):
        if arr[i][0] == arr[i][n-1]:
            continue
        elif arr[i][0] < arr[i][n-1]:
            asc= True
            break
        else:
            break
        
    result = []
    for j in range(k):
        result.extend(arr[j])
        
    if asc:
        result.sort()
    else:
        result.sort(reverse=True)
    return result

        
