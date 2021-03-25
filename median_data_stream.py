class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.min_heap.append(num)
        self.min_heap.sort()
        

    def findMedian(self) -> float:
        len_heap = len(self.min_heap)

        mid_el = len_heap//2
        if len_heap%2 ==0:
            median =  (self.min_heap[mid_el-1] + self.min_heap[mid_el])/2
        else:
            median = self.min_heap[mid_el]
        return median
