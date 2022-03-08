
## Memo Recursive solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s,wordDict, memo):
            if len(s) == 0:
                return True
            
            for word in wordDict:
                prefix = s[0: len(word)]
                
                if prefix == word and helper(s[len(word):], wordDict, memo):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
                
                    
                    
        
        memo = {}
        return helper(s, wordDict, memo)
