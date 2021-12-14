class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # print(self.stack)
        
    def pop(self) -> int:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        first, tmp, mx_id = True, None, None
        
        for i, vl in enumerate(self.stack):
            if first:
                tmp, mx_id = vl, i
                first = False
            else:
                if tmp < vl:
                    tmp, mx_id = vl, i
                elif tmp == vl and i > mx_id:
                    mx_id = i
        print(self.stack, mx_id) 
        self.stack.pop(mx_id)
        return tmp


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
