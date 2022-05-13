class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(i)
            print(ans)
        return ans.values()
        
        
        
 # Representing each string as count of alphabets list of 26.
 For same count of  string : will be same combination 
 ex: aabb --> [2, 2, 0, 0, ,0 0, 0, ,0 ,0 ,0 ,0 0, 0, ,0 0, 0, 0, ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 0, ,0 ,0 ,0 0, 0, 0, 0, 0, 0 .....]
 ex: aaabcccc---> [3, 1, 3, 0, ,0 0, 0, ,0 ,0 ,0 ,0 0, 0, ,0 0, 0, 0, ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 0, ,0 ,0 ,0 0, 0, 0, 0, 0, 0 .....]'
 
