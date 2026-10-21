class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        small = prices[0]
        profit = [0]
        for i in range(len(prices)):
            if prices[i] <= small:
                small = prices[i]
            else:
                profit.append(prices[i]-small)
        return max(profit)