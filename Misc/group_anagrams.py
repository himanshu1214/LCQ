class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        f_res = []
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp not in res:
                res[tmp] = [i]
            else:
                res[tmp].append(i)
                
        for k, v in res.items():
            f_res.append(v)
        return f_res
