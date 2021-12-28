class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = [ord(i) - ord('a') for i in s1]
        s2 = [ord(j) - ord('a') for j in s2]

        end=len(s1)
        start = 0
        while end <= len(s2):
            if sorted(s1) == sorted(s2[start:end]):
                return True
            else:
                start += 1
                end += 1
        return False
