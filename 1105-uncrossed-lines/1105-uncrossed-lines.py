class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2)+ 1)] for _ in range(len(nums1) + 1)]
        n1 = len(nums1)
        n2 = len(nums2)

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

        