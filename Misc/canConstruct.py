from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_dic = defaultdict(int)
        
        mag_dict = defaultdict(int)
        
        for i in ransomNote:
            ran_dic[i] += 1
            
        for j in magazine:
            mag_dict[j] += 1
            
        
        for k in ran_dic:
            if k not in mag_dict or (ran_dic[k] > mag_dict[k]):
                return False
            
        return True
