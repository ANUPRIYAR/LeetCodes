class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)    
        dp = [[0 for _ in range(2)]for _ in range(len(prices) + 2)]

        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j == 1:
                    dp[i][j] = max(dp[i+1][0] - prices[i], dp[i+1][1])
                else:
                     c1 = dp[i + 2][1] + prices[i]
                     c2 = dp[i+1][0]
                     dp[i][j] = max(c1, c2)
        return dp[0][1]

    