class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        print(s, pattern)
        start, visited = 0, defaultdict(str)
        while start < len(pattern):
            if (pattern[start] not in visited and s[start] not in visited.values()):
                visited[pattern[start]] = s[start]
            else:
                if (visited[pattern[start]] == s[start]):
                    start += 1
                    continue
                else:
                    return False
            
            start +=1
            print(visited)
        return True
