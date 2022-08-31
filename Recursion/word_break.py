class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_map = {}
        def dfs(s, wordDict):
            if not s:
                return True
            if s in hash_map:
                return hash_map[s]
            
            for word in wordDict:
                if s.startswith(word):
                    val =  dfs(s[len(word):], wordDict)
                    hash_map[s] = val
                    if val:
                        return True
                    
            return False
        
        return dfs(s, wordDict)
