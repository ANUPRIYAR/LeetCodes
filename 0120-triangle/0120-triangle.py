class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[0 for _ in range(rows)] for _ in range(rows)]

        for j in range(rows):
            dp[rows -1][j] = triangle[rows-1][j]

        for i in range(rows -2, -1, -1):
            for j in range(i, -1, -1):
                takesameindex = triangle[i][j] + dp[i + 1][j]
                takenextindex = triangle[i][j] + dp[i+1][j + 1]
                dp[i][j] = min(takesameindex, takenextindex)
        # print(dp)            
        return dp[0][0]
        