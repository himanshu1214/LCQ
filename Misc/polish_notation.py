class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["*", "/", "-", "+"]:
                sym = i
                el1 = int(stack.pop())
                el2 = int(stack.pop())
                if sym == "+":
                    stack.append(el1 + el2)
                elif sym == "-":
                    stack.append(el2 - el1)
                elif sym == "*":
                    stack.append(el1 * el2)
                elif sym == "/":
                    stack.append(el2 / el1)
                
            else:
                stack.append(i)
        return int(stack[0])
