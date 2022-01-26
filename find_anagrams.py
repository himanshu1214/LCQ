class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        if len(p) > len(s):
            return []
        p_hashmap = Counter(p)
        s_hashmap = Counter()
        len_s, len_p = len(s), len(p)
        start = 0
        ana = []
        # print(p)
        while start < len_s:
            s_hashmap[s[start]] += 1
            
            if start >= len_p:
                if s_hashmap[s[start - len_p]] == 1:
                    del s_hashmap[s[start - len_p]]
                else:
                    s_hashmap[s[start - len_p]] -= 1
            

            if p_hashmap == s_hashmap:
                ana.append(start- len_p +1)
            start += 1
            
        return ana
