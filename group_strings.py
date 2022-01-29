class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        def get_chardiff(ch):
            val = ""
            for i in range((len(ch)-1)):
                if ord(ch[i+1]) > ord(ch[i]):
                       val += str(ord(ch[i+1]) - ord(ch[i])) + "#"
                else:
                       val += str(ord(ch[i+1]) - ord(ch[i]) + 26) + "#"
            return val
        
        res = defaultdict(list)
        for _str in strings:
            if len(_str)>1:
                _hash = get_chardiff(_str)
                print(_str, _hash)
                res[_hash].append(_str)
            else:
                res["$"].append(_str)

        res = [i for i in res.values()]
        return res
