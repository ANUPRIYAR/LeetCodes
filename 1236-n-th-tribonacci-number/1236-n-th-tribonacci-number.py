class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        dp = [0 for _ in range(n+1)]
        dp[0], dp[1]= 0, 1
        dp[2]= 1
        for i in range(3, n +1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]



        