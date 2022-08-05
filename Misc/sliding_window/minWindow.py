class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        left = 0
        res = float('inf')
        reslen = [-1, -1]
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for i in range(len(t)):
            t_map[t[i]] += 1
            
        have, need = 0 , len(t_map)
        
        for r in range(len(s)):
            s_map[s[r]] += 1
            # here we check the keys and values are equal
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1
                 
            while have == need:
                if (r - left + 1) < res:
                    reslen = [left, r]
                    res = r - left + 1    

                s_map[s[left]] -= 1
                    
                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1
            print(have, need)        
        return s[reslen[0]: reslen[1]+1] if res != float('inf') else ""
