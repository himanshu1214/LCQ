class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        result = []
        def helper(s, ind, slate):
            #Base case
            if ind == len(s):
                result.append(''.join(slate[:]))
                return
            
            if s[ind].isdigit():
                slate.append(S[ind])
                helper(s, ind+1, slate)
                slate.pop()
            else:
                slate.append(s[ind].lower())
                helper(s, ind+1, slate)
                slate.pop()
                slate.append(s[ind].upper())
                helper(s, ind+1, slate)
                slate.pop()
        helper(S, 0, [])
        return result
                
            
                
