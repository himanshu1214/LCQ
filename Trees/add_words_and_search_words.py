# Time Complexity: O(N) -- in the worst case we traverse all the nodes of the trie
# Space Complexity O(N) --  only for call stack which in worse case will be O(N) for skewed tree
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofWord = True

    def search(self, word: str) -> bool:
        
        def dfs(index, root):
            curr = root
            for c in range(index, len(word)):
                if word[c] == ".":
                    for child_node in curr.children.values():
                        if dfs(c + 1, child_node):
                            return True
                    return False
                else:
                    if word[c] not in curr.children:
                        return False
                    curr = curr.children[word[c]]
            return curr.endofWord
        return dfs(0, self.root)
