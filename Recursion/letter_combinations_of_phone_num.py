class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map_num_letter = {"1": "", 
                          "2": ["a", "b", "c"], 
                          "3": ["d", "e", "f"],
                          "4": ["g", "h", "i"],
                          "5": ["j", "k", "l"],
                          "6": ["m", "n", "o"],
                          "7": ["p", "q", "r", "s"],
                          "8": ["t", "u", "v"],
                          "9": ["w", "x", "y", "z"]
                         }
        
        res = []
        def dfs(digits, slate, index):
            if index > len(digits)-1:
                res.append("".join(slate[:]))
                return 
    
            for alp in map_num_letter[digits[index]]:
                slate.append(alp)
                dfs(digits, slate, index+1)
                slate.pop()
        dfs(digits, [], 0)
        return res
