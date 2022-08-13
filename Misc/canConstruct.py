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

    
# Alternate
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_dic = [0 for i in range(26)]
        
        mag_dict = [0 for j in range(26)]
        
        for i in ransomNote:
            ran_dic[int(ord(i.upper()) - 65)] += 1
            
        for j in magazine:
            mag_dict[int(ord(j.upper())) - 65] += 1
            
        
        for k in range(len(ran_dic)):
            if ran_dic[k] and mag_dict[k] < ran_dic[k]: 
                return False
            
        return True
