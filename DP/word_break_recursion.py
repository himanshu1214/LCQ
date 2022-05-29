class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def helper(s, wordDict):
            if len(s)< 0:
                return False
            
            if len(s) == 0:
                return True
            
            if len(s) in memo:
                return memo[len(s)]
            
            res = []
            for word in wordDict:
                if s[:len(word)] == word:
                    res.append(helper(s[len(word):], wordDict))
            memo[len(s)] = any(res)
            return memo[len(s)]
        
        return helper(s, wordDict)
