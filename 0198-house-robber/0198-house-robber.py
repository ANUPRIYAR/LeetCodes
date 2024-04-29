class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        n = len(nums)
        dp = [0 for i in range(n)]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, n):
            steelcurrent = nums[i] + dp[i-2]
            skipcurrent = dp[i-1]
            dp[i] = max(steelcurrent, skipcurrent)

        return dp[n-1]

        

