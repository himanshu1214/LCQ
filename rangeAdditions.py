class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0 for i in range(length)]

        for update in updates:
            start, end, val = update[0], update[1], update[2]
            print(start, end, val)
            arr[start] += val
            if end + 1 < len(arr):
                arr[end+1] -= val
        out = [0 for i in range(length)]
        tmp = 0
        
        for j in range(len(arr)):
            tmp += arr[j]
            out[j] = tmp

        return out
