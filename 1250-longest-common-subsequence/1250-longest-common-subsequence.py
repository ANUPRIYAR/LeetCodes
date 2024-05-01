class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(n1 + 1):      # if i == len(text1) or j == len(text2):  return 0
            dp[i][n2] = 0

        for j in range(n2 + 1):        # if i == len(text1) or j == len(text2):  return 0
            dp[n1][j] = 0

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] =  1  + dp[i+1][j+1]
                else:
                    c1 = dp[i+1][j]
                    c2 = dp[i][j+1]
                    dp[i][j] = max(c1, c2)
        return dp[0][0]  