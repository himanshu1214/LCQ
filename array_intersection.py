#1213. Intersection of Three Sorted Arrays
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ind1 = 0
        ind2 = 0
        ind3 = 0
        common = []
        while ind1<= len(arr1)-1 and ind2<= len(arr1)-1 and ind3<= len(arr1)-1:
            if arr1[ind1] == arr3[ind3] == arr2[ind2]:
                common.append(arr1[ind1])
                ind1 +=1 
                ind2 += 1
                ind3 += 1
                
            elif arr1[ind1] < arr2[ind2]:
                ind1 +=1
            elif arr2[ind2] < arr3[ind3]:
                ind2 += 1
            else:
                ind3 +=1
            
        return common
            
