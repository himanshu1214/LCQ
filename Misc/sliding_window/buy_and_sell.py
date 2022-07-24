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
                
 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 10000
        max_selloff = 0
        for i in prices:
            if i < min_val:
                min_val = i
            if i - min_val > max_selloff:
                max_selloff = i - min_val
                
        return max_selloff
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                buy = prices[i]
            else:
                if prices[i] < buy:
                    buy = prices[i]
                elif prices[i] > buy:
                    sell = prices[i]
                    if profit < sell - buy:
                        profit = sell - buy
                    
        return profit
