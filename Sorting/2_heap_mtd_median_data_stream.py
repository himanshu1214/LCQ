import heapq
class Median():
    def __init__(self):
        self.mn_heap = []
        self.mx_heap = []

    def Addnum(self, num):
        heapq.heappush(self.mx_heap, -1*num)
        heapq.heappush(self.mn_heap, -1*self.mx_heap[0])
        heapq.heappop(self.mx_heap)

        if len(self.mx_heap) < len(self.mn_heap):
            heapq.heappush(self.mn_heap, num)
            heapq.heappush(self.mx_heap, -1*self.mn_heap[0])
            heapq.heappop(self.mn_heap)
    
    def MedianFind(self):
        if len(self.mx_heap) > len(self.mn_heap):
            return -1*self.mx_heap[0]
        else:
            return (-1*self.mx_heap[0] + self.mn_heap[0])/2
obj = Median()
for i in [3, 4, 5]:
    obj.Addnum(i)

    print(obj.MedianFind())

# min_heap=[]

# max_heap=[]

# Iteration1:
# num = 1
# min_heap=[]

# max_heap=[1]

# Iteration2:
# num = 2
# min_heap=[2]

# max_heap=[1]

# Iteration3:
# num = 3
# min_heap=[3]

# max_heap=[1, 2]


# Iteration4:
# num = 4
# min_heap=[4, 3]

# max_heap=[1, 2]


# Iteration5:
# num = 5
# min_heap=[5, 4]

# max_heap=[1, 2, 3]

# Iteration6:
# num = 16
# min_heap=[16, 5, 4]

# max_heap=[1, 2, 3]

# Iteration7:
# num = 10
# min_heap=[16, 10,  5]

# max_heap=[1, 2, 3, 4]

# Iteration8:
# num = 8
# min_heap=[16, 10, 8, 5]

# max_heap=[1, 2, 3, 4]

# Iteration9:
# num = 12
# min_heap=[16, 12, 10, 8]

# max_heap=[1, 2, 3, 4, 5]
