class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        _s = "".join([i for i in s if i != '-'])

        if len(_s) % k ==0:
            num_chars_in_grps = len(_s)//k
            print(num_chars_in_grps)
            chars = ""
            tmp = 0
            for i in range(k, len(_s)+1, k):
                chars  += _s[tmp:i] + "-"
                tmp = i
            print(chars)
            return chars[:-1].upper()
        else:
            rem = len(_s) % k
            chars = ""
            print(chars)
            tmp = 0
            for i in range(rem, len(_s)+1, k):
                print(chars)
                chars += _s[tmp:i] + "-"
                tmp = i
            return chars[:-1].upper()
