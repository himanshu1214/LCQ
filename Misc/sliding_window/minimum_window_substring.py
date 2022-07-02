class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import sys
        from collections import defaultdict
        t_map = defaultdict(int)
        for i in t:
            t_map[i] += 1
            
        s_map = {j : 0 for j in t}

        def have_ct(s_map):
            ct = 0
            for i in s_map:
                if s_map[i]>= t_map[i]:
                    ct += 1
            return ct

        need_ct = len(t_map)
        ptr_one = 0
        ptr_two = 0
        res = ("", sys.maxsize)
        while ptr_one < len(s) and ptr_two < len(s):
            if s[ptr_two] in t_map: # check s in t
                s_map[s[ptr_two]] += 1 # increment hash_map for string s by 1
                while have_ct(s_map) >= need_ct: # Check the have_counts vs need_counts
                    if res[1] > (ptr_two - ptr_one): # update the window size 
                        res = (s[ptr_one: ptr_two+1], len(s[ptr_one: ptr_two+1]))
                    if s[ptr_one] in s_map: # reduce s_map count
                        if s_map[s[ptr_one]] > 0:
                            s_map[s[ptr_one]] -= 1
                    ptr_one += 1
            ptr_two += 1

        return res[0]
