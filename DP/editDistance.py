class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        table = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            table[i][0] = i
            
        for j in range(len(word2)+1):
            table[0][j] = j
        print(table)
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1] :
                    replace_cost = 0
                else:
                    replace_cost = 1

                table[i][j] =  min(table[i-1][j] +1 , table[i][j-1] +1, table[i-1][j-1] + replace_cost)
 
        return table[len(word1)][len(word2)] 
