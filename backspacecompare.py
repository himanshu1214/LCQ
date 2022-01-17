#with space O(n) and time O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_start, t_start = 0, 0
        
        de = 0
        s_stack = []
        while s_start < len(s) :
            if s[s_start] == "#":
                if len(s_stack) >0:
                    s_stack.pop()
            else:
                s_stack.append(s[s_start])
            s_start += 1
        
        t_stack = []
        while t_start < len(t) :
            if t[t_start] == "#":
                if len(t_stack) >0:
                    t_stack.pop()
            else:
                t_stack.append(t[t_start])
            t_start += 1
            
        i = 0
        if len(s_stack) != len(t_stack):
            return False
        print(s_stack, t_stack)
        while i < len(s_stack):
            if s_stack[i] != t_stack[i]:
                return False
            i += 1
        return True
