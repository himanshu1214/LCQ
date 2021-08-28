class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        if not s:
            return 0
        from collections import defaultdict
        coll = defaultdict()
        i = 0
        j = 0
        while j < len(s):
            dist = len(set(s[i:j+1]))
            if dist <=2:
                coll[s[i:j]] = len(s[i:j+1])
                j += 1
            else:
                i += 1
        val = max(coll.values())
        return val
