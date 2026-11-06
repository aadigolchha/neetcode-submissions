class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest_buy:
                lowest_buy = prices[i]
            elif prices[i] - lowest_buy > max_profit:
                max_profit = prices[i] - lowest_buy
            else:
                continue
        return max_profit 

            



