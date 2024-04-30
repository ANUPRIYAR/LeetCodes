import math

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0]) 
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        dp[0][1] = 1 

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if not obstacleGrid[i-1][j-1]:
                    moveright = dp[i][j-1]
                    movedown = dp[i-1][j]
                    dp[i][j] = moveright + movedown
        return dp[-1][-1]
        