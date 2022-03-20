class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict, Counter
        mp = defaultdict(list)
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]].append([i, 1])
            else:
                mp[s[i]][0][1] += 1
                
        print(mp)
        for ind, val in mp.items():
            print(val)
            if val[0][1] == 1:
                return val[0][0]
            
        return -1
