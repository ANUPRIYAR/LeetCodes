class Solution:
    def numTrees(self, n: int) -> int:
        if n ==0 or n ==1:
            return 1
            
        dp = [0 for _ in range(n +1)]
        dp[0]= 1

        ans = 0
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]

        return dp[n]