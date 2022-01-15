# 588. Design In-Memory File System

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isfile = False
        self.content = ""
        self.filename = ""
    
    
class FileSystem:

    def __init__(self):
        self.trie = TrieNode()

#     def node_traverse(self, path):
#         curr = self.trie
#         paths = [''] if path == "/" else path.split("/")[1]
        
#         for _dir in paths:
#             curr = curr.child(_dir)
#         return curr
    
    def ls(self, path: str) -> List[str]:
        curr = self.trie
        paths = [] if path == "/" else path.split("/")[1:]

        for _dir in paths:
            curr = curr.child[_dir]
            
        if curr.isfile:
            return [curr.filename]
        d = []
        for cu in curr.child:
            d.append(cu)
        return sorted(d)
            
            
        
    def mkdir(self, path: str) -> None:
        paths = path.split("/")[1:]
        curr = self.trie
        
        for p in paths:
            curr = curr.child[p]
            curr.name = p
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.trie
        filepath = filePath.split("/")[1:]
        for p in filepath:
            curr = curr.child[p]
            curr.filename = p
        curr.isfile = True
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.trie
        filepath = filePath.split("/")[1:]
        for p in filepath:
            curr = curr.child[p]
            
        if curr.isfile:
            return curr.content
        
    
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
