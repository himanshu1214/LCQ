class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        account_mail = defaultdict(list)
        
        visited_account = [False]*len(accounts)
        for i in range(len(accounts)):
            name, acc_list = accounts[i][0], accounts[i][1:]
            for acc in acc_list:
                account_mail[acc].append(i)
                
        def dfs(key,  acc_set):
            
            if visited_account[key]:
                return 
            visited_account[key] = True
            
            for j in range(1, len(accounts[key])):
                email = accounts[key][j]
                acc_set.add(email)
                for accs_num in account_mail[email]:
                    dfs(accs_num, acc_set)
                    
        res = []
        for i in range(len(accounts)):
            if visited_account[i]:
                continue
            name, acc_set = accounts[i][0], set()
            dfs(i, acc_set)
            res.append([name] + sorted(acc_set))
        return res
