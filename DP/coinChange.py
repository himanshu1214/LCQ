class Solution:
    import sys
    def coinChange(self, coins: List[int], amount: int) -> int:
        #                         1                 2               5
        #                 1       2     5
        #             1   2   5 
        #           
        #          False 
                
        memo = [None for i in range(amount + 1)]
        def helper(coins, remain):
            if remain < 0:
                return -1

            if remain == 0:
                return 0
            if memo[remain] != None:
                return memo[remain]
            
            minCount = sys.maxsize
            for coin in coins:
                count = helper(coins, remain-coin)
                if count == -1:
                    continue
                minCount = min(minCount, count + 1)
            memo[remain] = -1 if minCount == sys.maxsize else minCount
            return memo[remain]
        
        return helper(coins, amount)
