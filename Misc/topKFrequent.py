class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        hash_tabl = defaultdict(int)
        for i in words:
            hash_tabl[i] += 1
            
        top_k = [k for k, v in sorted(hash_tabl.items(),  key=lambda item: (-item[1], item[0]))]

        return top_k[:k]
