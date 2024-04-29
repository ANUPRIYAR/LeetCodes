class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for x in range(len(nums) + 1)]
        return self.helper(dp, nums, 0)

    def helper(self,dp,  nums, cur_idx):
        if cur_idx >= len(nums):
            return 0

        if dp[cur_idx] == -1:
            steelcurrent = nums[cur_idx] + self.helper(dp, nums, cur_idx + 2)
            skipcurrent = self.helper(dp, nums, cur_idx + 1)
            dp[cur_idx] = max(steelcurrent, skipcurrent)

        return dp[cur_idx]