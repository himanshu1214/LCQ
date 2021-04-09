import random
import sys
def quickSort(arr):
    # if not arr:
    #     return []
    # if len(arr) ==1 :
    #     return arr
    

    def helperquick(arr, start, end):
        if start >= end:
            return print(f'Exiting the recursion : {arr[start]}')
        
        start = start
        end = end
        pivot = random.randrange(start, end)
        print(f'pivot is : {pivot}')
        arr[pivot], arr[start] = arr[start], arr[pivot]
        orange= start
        green = start+1
        while green <= end:
            if arr[green] < arr[start]:
                orange +=1
                arr[green], arr[orange] = arr[orange], arr[green]    
                green += 1            
            else:
                green += 1
        arr[start], arr[orange] = arr[orange], arr[start]
        k = 4
        print(orange, k, arr)
        # sys.exit()
        if (len(arr)-1 - k) == orange:
            print(f'Exiting the recursion : {arr[orange]}')
        elif (len(arr)-1 - k) > orange:
            helperquick(arr, orange+1, end)
        elif (len(arr)-1 - k) < orange:
            helperquick(arr, start, orange-1)

    helperquick(arr, 0, len(arr)-1)
    # return arr
    
arr = [9, 8, 7, 6, 5, 4, 3, 2,1]
print(quickSort(arr))
