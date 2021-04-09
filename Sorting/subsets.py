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

#Space Complexity :
# Input + Aux + Output
# O(n) + For one call stack O(n) at max + Total (2^n) leaves* n/2 avg size of the leaves
# O(n) + O(n) + O(2^n*n) ~ O(2^n*n)

#Time Complexity
# leave worker + Internal Node worker
# O(2^n *n/2) avg (n/2) amount of time to create copy the aux list to final array  +  O(2^n-1*1) constant time to add an element into list ~ O(2^n)
# O(2^n *n/2) + O(2^n-1*1) ~ O(2^n*n)

