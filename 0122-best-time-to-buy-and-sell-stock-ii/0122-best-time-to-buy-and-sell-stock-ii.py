class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if start < prices[i]:
                maxprofit += prices[i]- start
            start = prices[i]

        return maxprofit
        