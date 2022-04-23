class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
 
            if i not in ["-", "*", "/", "+"]:
                stack.append(i)
            else:
                right = stack.pop()
                left = stack.pop()
                if i == "+":
                    evaluate = int(left) + int(right)
                if i == "-":
                    evaluate = int(left) - int(right)
                if i == "*":
                    evaluate = int(left) * int(right)
                if i == "/":
                    evaluate = int(left) / int(right)
    
                stack.append(evaluate)
        return int(stack[0])
