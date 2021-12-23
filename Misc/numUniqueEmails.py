#Google Interview Q

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        import re
        from collections import defaultdict
        dc = defaultdict(set)
        
        for i in emails:
            val = i.split("@")[0].split("+")[0]
            _remove_dot_pattern  = re.compile('\W')
            clean_val = re.sub(_remove_dot_pattern, '', val)
            dc[i.split("@")[1]].add(clean_val)
            
        ln = 0
        for i in dc.values():
            ln += len(i)
        
        return ln
