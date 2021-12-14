from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit, min_pos = 0, 0
        for i in range(len(prices)):
            if prices[i] - prices[min_pos]> max_profit:
                max_profit = prices[i] - prices[min_pos]
            elif prices[i] - prices[min_pos] < 0:
                min_pos = i
        return max_profit
                
