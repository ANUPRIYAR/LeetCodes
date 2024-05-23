import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        return self.helper(days, costs, 0, dp)

    def helper(self, days, costs, idx, dp):
        if idx >= len(days):
            return 0
        if idx not in dp:
            onedaypass = costs[0] + self.helper(days, costs, idx + 1, dp)
            sevendayindex = bisect_left(days, days[idx] + 7)
            sevendaypass = costs[1] + self.helper(days, costs, sevendayindex, dp)

            month_index = bisect_left(days, days[idx] + 30)
            monthpass = costs[2] + self.helper(days, costs, month_index, dp)
            dp[idx] = min(onedaypass,sevendaypass, monthpass)
        return dp[idx]