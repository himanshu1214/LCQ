class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        if len(s) == 0:
            return True
        pairs=  {'(': ')', '{': '}', '[':']'}
        
        if s[0] in pairs.values():
            return False
        
        for i in range(len(s)):
            if s[i] in pairs.keys():
               res.append(s[i])
            else:
                if len(res)>0:
                    elm = res.pop()
                    if pairs[elm] == s[i]:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(res)==0:
            return True
        else:
            return False
                