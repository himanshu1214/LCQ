def merge_sort(arr):
    

    def helpermergesort(arr, start, end):

        if start >= end:
            return 
        

        #Divide
        mid = (end + start)//2
        helpermergesort(arr, start, mid)
        helpermergesort(arr, mid + 1, end)

        #Merge
        lstart = start
        rstart = mid + 1
        aux = []
        while lstart<= mid and rstart <= end:
            if arr[lstart] < arr[rstart]:
                aux.append(arr[lstart])
                lstart += 1
            else:
                aux.append(arr[rstart])
                rstart += 1
        
        while lstart<= mid:
            
                aux.append(arr[lstart])
                lstart += 1
        while rstart<= end:
                aux.append(arr[rstart])
                rstart += 1
        arr[start:end+1]=aux
    
    helpermergesort(arr, 0, len(arr)-1)
    return arr
    

arr = [9, 8, 7, 6, 5, 4, 3, 2,1]
print(merge_sort(arr))
# for i in arr:
#     print(i)
