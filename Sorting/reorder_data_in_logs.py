from collections import defaultdict
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []
        let, dig = [], []

        for i in range(len(logs)):
            list_c = logs[i].split(" ")
            val = list_c[1:]
            # val.sort()
            key = list_c[0]
            if val[0].isdigit():
                dig.append(logs[i])
            else:
                let.append(logs[i])
            
        let.sort(key=lambda kv: (kv.split()[1:], kv.split()[0]))
        
        res = let + dig
        return res
            
        
