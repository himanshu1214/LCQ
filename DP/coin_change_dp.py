class Solution:
    import sys
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [sys.maxsize for i in range(amount)]
        for i in range(1, amount+1):
            for j in coins:
                if (i - j) >= 0:
                    dp[i] = min(dp[i], dp[i - j] + 1)

        return -1 if dp[-1] == sys.maxsize else dp[-1]
                    
