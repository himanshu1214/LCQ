class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for str_s in s.split(" "):
            k = str_s[::-1]
        
            res.append(k)
        f_res = " ".join(res)
        return f_res
