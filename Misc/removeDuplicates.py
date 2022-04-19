    def removeDuplicates(self, s: str) -> str:
        if s:
            stack = [s[0]]

        for i in s[1:]:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
            
        return "".join(stack)
