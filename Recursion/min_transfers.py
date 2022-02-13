class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # 0 -> 1   ----> $10
        # 2 -> 0   ----> $5
        
        # 1 --> 0  ----> $5
        # 1 --> 2  ----> $5
        
        #Ex: 0 give 1 -> $10
        #    1 give 0 -> $1
        #    1 give 2 -> $5
        #    2 give 0 -> $5
        import collections
        import sys
        debt_hash = collections.defaultdict(int)
        
        # Making overall graph for transactions
        for g, t, dollar in transactions:
            debt_hash[g] += dollar
            debt_hash[t] -= dollar
        
        # Create list for ppl with non zero debt
        nt_debt_list = []
        for dollar in debt_hash.values():
            if dollar != 0:
                nt_debt_list.append(dollar)
                
        
        # traversing across the graph for ppl with net non negative debts
        def dfs(nt_debt_list, st_ind, transaction):
            # for non greedy way meaning any checking the transaction.
            # skipping settled ppl
            while st_ind < len(nt_debt_list) and nt_debt_list[st_ind] == 0:
                st_ind += 1   
            
            #Base condition:
            if st_ind + 1 >= len(nt_debt_list):
                return transaction
            else:
                for i in range(st_ind +1, len(nt_debt_list)):
                    if nt_debt_list[i] + nt_debt_list[st_ind] == 0:
                        nt_debt_list[i] += nt_debt_list[st_ind]
                        min_transaction = dfs(nt_debt_list, st_ind + 1, transaction+1)
                        nt_debt_list[i] -= nt_debt_list[st_ind]
                        return min_transaction
                min_transaction = sys.maxsize
                
                for i in range(st_ind + 1, len(nt_debt_list)):
                    if nt_debt_list[i]*nt_debt_list[st_ind] <0:
                        nt_debt_list[i] += nt_debt_list[st_ind]
                        min_transaction = min(min_transaction, dfs(nt_debt_list, st_ind + 1, transaction+1))
                        nt_debt_list[i] -= nt_debt_list[st_ind]

                return min_transaction
            
        return dfs(nt_debt_list, 0, 0)
