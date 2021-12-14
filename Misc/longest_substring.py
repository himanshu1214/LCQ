class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        res = []
        tmp = []
        size = 0
        while start <= end and end < len(s):
            if s[end] not in tmp[start:end]:
                tmp.append(s[end])
                end += 1
            else:
                if end - start > size:
                    size = end - start
                start += 1
        if (end-start) > size:
            size = end - start

        return size
