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
        
 class Solution:
    def isValid(self, s: str) -> bool:
        #{([])}
        if len(s) % 2 != 0:
            return False
        
        if not s:
            return False
        
        dic = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in s:
            if i in dic.values():
                
                if not len(stack) : 
                    return False
                if stack[-1] not in dic:
                    return False
                
                elif dic[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
  
            else:
                stack.append(i)
            
        return len(stack) == 0 and True
                
