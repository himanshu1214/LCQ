class Solution:
    def decodeString(self, s: str) -> str:
        
        #> 3[a]2[bc]
        # > 
        stack = []
        num = []

        bracket = 0
        for i in range(len(s)):
            if not s[i] == "]":
                stack.append(s[i])
            elif s[i] == "]":
                num = ""
                res = ""
                ele = ""
                # pop characters from stack
                while stack and stack[-1].isalpha():
                    val = stack.pop()
                    if val.isalpha():
                        ele += val
                #pop [ from stack
                stack.pop()
                # pop numbers from stack
                while stack and stack[-1].isdigit():
                    val = stack.pop()
                    if val.isdigit():
                        num +=  val
                # Get number
                num = num[::-1]

                # Flatten the characters
                res += int(num)*ele
                
                # Push the chars back into stack
                for i in range(len(res) -1, -1, -1):
                    stack.append(res[i])
        return "".join(stack)
                
