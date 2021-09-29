#Fail on last test case: Needs optimization 

class Trie():
    def __init__(self):
        self.head = {}

    def add(self, word):
        curr = self.head
        for i in word:
            if i not in curr:
                 curr[i] = {}
            curr = curr[i]
        curr["*"] = True

        
    def search(self, word: str):
        curr = self.head
        for i in word:
            if  i not in curr:
                return False
            curr = curr[i]
        return "*" in curr

    def startswith(self, prefix: str):
        curr = self.head
        for i in prefix:
            if i not in curr:
                return False
            curr = curr[i]
        return True
                  
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        row, col  = len(board), len(board[0])
        tr = Trie()
        
        for word in words:
            tr.add(word) 
            
        def helper(rw, cl, path):

            # Check the row and col bounds and if string doesnot starts with 
            # and is not visited {this is taken care through in place value change}
            
            if rw not in range(row) or cl not in range(col):
                return
            
            letter = board[rw][cl]
            # this is to see if word some exist
            temp = path + [board[rw][cl]]
            string = "".join(temp)
            
            # actively remove the word 
            if not tr.startswith(string):
                return
  
            # this is to see if word some exist
            elif tr.search(string):
                result.add(string)
                
 
            tmp = board[rw][cl]
            board[rw][cl] = "0"
            helper(rw+1, cl, temp) 
            helper(rw-1, cl, temp) 
            helper(rw, cl+1, temp) 
            helper(rw, cl-1, temp) 
            board[rw][cl] = tmp
                
        result = set()
 
            
        for i in range(row):
            for j in range(col):
                helper(i, j, [])
                
        return result
