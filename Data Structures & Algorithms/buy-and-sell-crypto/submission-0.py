class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(0,len(prices)):
            for y in range(i, len(prices)):
                if prices[y]-prices[i] > res:
                    res = prices[y]-prices[i]
        return res
            

