class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        hash_tab = defaultdict(int)
        left = 0
        right = 0
        res = 0
        while left <= right and right < len(s):
            hash_tab[s[right]] += 1
            while (right - left + 1) - max(hash_tab.values()) > k:
                hash_tab[s[left]] -= 1
                left += 1
            res = max(res, (right - left +1))  
            right += 1
        return res

    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        hash_tab = defaultdict(int)
        left = 0
        right = 0
        max_count = 0
        max_window_len = 0
        res = 0
        while left <= right and right < len(s):
            hash_tab[s[right]] += 1
            
            max_count = max(max_count,hash_tab[s[right]])
            
            while (right - left + 1) - max_count > k:
                hash_tab[s[left]] -= 1
                left += 1
            res = max(res, (right - left +1))  
            right += 1
        return res
