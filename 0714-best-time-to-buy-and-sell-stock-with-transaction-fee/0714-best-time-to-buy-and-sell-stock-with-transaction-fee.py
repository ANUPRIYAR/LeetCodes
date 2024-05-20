class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)]for _ in range(len(prices) + 1)]

        for i in range(n-1, -1, -1):
            for j in range(2):
                if j == 0:
                    dp[i][j] = max(dp[i+1][1] - prices[i],dp[i+1][0])
                else:
                    dp[i][j] = max(prices[i] - fee + dp[i+1][0], dp[i+1][1])
        return dp[0][0]