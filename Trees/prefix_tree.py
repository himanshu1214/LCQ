class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
 
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True

    
class TrieNode:
    def __init__(self):
        self.word =  False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        print(node.children)
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
                
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i in node.children:
                node = node.children[i]
            else:
                return False
        return node.word
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i in node.children:
                node = node.children[i]
            else:
                return False
        return True
