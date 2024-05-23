class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(len(s) + 2)]
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                single = dp[i + 1]

                multiple = 0
                if i < n -1  and 10 <= int(s[i] + s[i+1]) <= 26:
                    multiple = dp[i + 2]

                dp[i] = single + multiple
        return dp[0]