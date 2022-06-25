class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        start = 0
        end = len(s)
        left  = 0
        right = 0
        high_freq_item_in_string = defaultdict(int)
        win_size = 0
        while left < end and right < end:
            high_freq_item_in_string[s[right]] += 1
            
            sort_freq = sorted(high_freq_item_in_string.items(), key=lambda kv: kv[1])
            if (len(s[left:right+1]) - sort_freq[-1][1]) <= k:
                tmp_size = right + 1 -left
                if win_size < tmp_size:
                    win_size = tmp_size
            else:
                high_freq_item_in_string[s[left]] -= 1
                left += 1  
            right += 1
        return win_size
