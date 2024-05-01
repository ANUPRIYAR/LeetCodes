class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen = len(s)
        tlen = len(t)
        dp = [[0 for _ in range(len(t) + 1)] for _  in range(len(s) + 1 )]

        for i in range(slen +1):
            dp[i][tlen] = 1 

        # for j in range(tlen-1, -1, -1):
        #     dp[slen][j] += dp[slen][j+1] 

        for i in range(slen-1, -1, -1):
            for j in range(tlen -1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] += dp[i+1][j]

        return dp[0][0]


        