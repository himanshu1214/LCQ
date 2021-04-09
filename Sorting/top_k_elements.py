
#This question can easily solved with heaps in nlogn
#Can be solved with Bucket sort {not worked till now} in O(n)
#With Quick select,its within O(n) 

from random import randint
def quickSelect(arr, k):
    def helpersort(arr, start, end):
        if start >= end:
            print(f'the recursion is exiting {start}')
            return start
            # return f'the recursion is exiting {[i[1] for i in arr[start:]]}'
        pivot = randint(start, end)
        print(f'pivot : {pivot}')
        print(f'start : {start}')
        # print(f'end : {end}')
        print(f'arr : {[i[1] for i in arr]}')

        arr[pivot], arr[start] = arr[start], arr[pivot]
        orange = start 
        green = start + 1
        while green <= end:
            # print(arr[green][1], arr[start][1])
            if arr[green][1] < arr[start][1]:
                orange += 1
                arr[green], arr[orange] = arr[orange], arr[green]
                green += 1
            else:
                green += 1
        print(f'orange : {orange}')
        # print([i[1] for i in arr[orange:]])
        arr[orange], arr[start] = arr[start], arr[orange]
        print([i[1] for i in arr])
        # print(f'orange : {orange}')
        # print([i[1] for i in arr])
        if k-1 < orange: 
            helpersort(arr, start, orange-1)
        elif k-1 > orange: 
            helpersort(arr, orange+1, end)
        elif k-1 == orange: 
            print(f'the recursion is exiting {orange}')
            return orange
            # return arr[orange]
        
    aux = {}
    for num in nums:
        if num in aux: 
            aux[num] += 1
        else:
            aux[num] = 1
    aux_items = list(aux.items())
    k = helpersort(aux_items, 0, len(aux_items)-1)
    print(f'k val is {orange}')

nums = [1,1,1,2,2,3, 3, 4, 2, 1, 1, 1]
k = 2
print(quickSelect(nums, k))
