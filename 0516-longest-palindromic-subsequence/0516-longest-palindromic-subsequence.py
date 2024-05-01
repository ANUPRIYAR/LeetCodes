class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(n):
            dp[i][i] = 1

        for start in range(n-1, -1, -1):
            for end in range(start +1, n):
                if s[start] == s[end]:
                        dp[start][end] = 2 + dp[start +1][end - 1]
                else:
                    c1 = dp[start][end -1]
                    c2 = dp[start +1][end]
                    dp[start][end] = max(c1, c2)
        return dp[0][n-1]
    