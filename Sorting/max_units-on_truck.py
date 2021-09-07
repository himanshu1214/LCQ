class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        print(boxTypes)
        res = 0
        for box in boxTypes:
            for j in range(box[0]):
                if truckSize>0:
                    res += box[1]
                # print(res, box[1])
                truckSize -= 1
        return res
