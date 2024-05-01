import math
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)

        dp = [[math.inf for _ in range(len(word2) + 1) ]for _ in range(len(word1) + 1)]

        for i in range(w1 +1):
            dp[i][w2] =  w1 - i  

        for j in range(w2 +1):
            dp[w1][j] =  w2 - j

        for i in range(w1 -1, -1, -1):
            for j in range(w2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    # deletions
                    c1 = 1 + dp[i+1][j]
                    # insertions
                    c2 = 1 + dp[i][j+1]
                    # replacements
                    c3 = 1 + dp[i+1][j+1]
                    dp[i][j] = min(c1, c2, c3)

        return dp[0][0]