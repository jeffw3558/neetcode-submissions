class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        for i in range(0, len(prices)):
            if prices[i]< min_val:
                min_val = prices[i]
            elif prices[i]-min_val > profit:
                profit = prices[i]-min_val
            
        return profit
            

