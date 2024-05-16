class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        n = len(pairs)
        dp = [1] * len(pairs)

        maxlength = 1
        c1, c2 = 0, 0
        for i in range(1,n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[i] <=dp[j]:
                    dp[i] = dp[j] + 1
                    maxlength = max(maxlength, dp[i])
        return maxlength    