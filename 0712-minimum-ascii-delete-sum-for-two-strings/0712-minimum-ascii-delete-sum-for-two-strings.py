class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i in range(n1-1, -1, -1):
            dp[i][n2] = ord(s1[i]) + dp[i+1][n2]

        for j in range(n2-1, -1, -1):
            dp[n1][j] = ord(s2[j]) + dp[n1][j+1]


        for i in range(n1-1, -1 , -1):
            for j in range(n2-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j +1]
                else:
                    c1 = ord(s1[i]) +  dp[i + 1][j]
                    c2 = ord(s2[j]) + dp[i][j + 1]
                    dp[i][j] = min(c1, c2)

        return dp[0][0]
                    
                
                 






       