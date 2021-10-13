class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hash_map = defaultdict(list)
        for words in strs:
            sort_val = "".join(sorted(words))
            hash_map[sort_val].append(words)
        list_map = list(hash_map.values())
        return list_map
