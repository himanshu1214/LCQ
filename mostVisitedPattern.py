class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict, Counter
        from itertools import combinations
        
        score = defaultdict(list)
        for user,time,  web in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
            score[user].append(web)
        pattern = Counter()
        
        for user, web in score.items():
            comb = combinations(web, 3)
            set_comb = Counter(set(comb))
            pattern.update(set_comb)
        
        return max(sorted(pattern), key=pattern.get)
        
