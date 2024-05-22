class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = {}
        for i in range(n-1, -1, -1):
            next_index = i + questions[i][1] + 1
            attempt = questions[i][0] + dp.get(next_index, 0)
            skip = dp.get(i+1, 0)
            dp[i] = max(attempt, skip)
        return dp[0]