class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_lst = []
        t_lst = []
        s_ct = 0
        t_ct = 0
        for i in range(len(s)):
            if s[i] != "#":
                s_lst.append(s[i])
            else:
                if s_lst:
                    s_lst.pop()
                
            
            
            
        for j in range(len(t)):
            if t[j] != "#":
                t_lst.append(t[j])
            else:
                if t_lst:
                    t_lst.pop()
        return s_lst == t_lst
