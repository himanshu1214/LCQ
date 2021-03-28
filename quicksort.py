import random
def quickSort(arr):
    if not arr:
        return []
    if len(arr) ==1 :
        return arr
    return helperquick(arr, 0, len(arr)-1)

def helperquick(arr, start, end):
    if start >= end:
        return 
    if len(arr) ==1 :
        return arr
    start = start
    end = end
    pivot = random.randrange(start, end)
    arr[pivot], arr[start] = arr[start], arr[pivot]
    orange= start
    green = start+1
    i = 0
    while green <= end:
        if arr[green] < arr[start]:
            orange +=1
            arr[green], arr[orange] = arr[orange], arr[green]    
            green += 1            
        else:
            green += 1
    arr[start], arr[orange] = arr[orange], arr[start]
    print(arr)
    helperquick(arr, start, orange-1)
    helperquick(arr, orange+1, end)
    
    

print(quickSort([9, 8, 7, 6, 5, 4, 3, 2,1]))
                

