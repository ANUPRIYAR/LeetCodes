class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0 for _ in range(3)]for _ in range(2)]for _ in range(len(prices) + 1)]   # We take 1 + k as well as 1 + n
        n  = len(prices)
        
        # We are omiting the base cases since the values are already 0

        for i in range(n-1, -1, -1):   #Iterate backwards as usual
            for j in range(2):
                for k in range(1,3):    #this we will take from 1, 3, since value at k=0 should be 0
                    if j == 0:
                        dp[i][j][k] = max(dp[i+1][1][k]- prices[i], dp[i+1][0][k])
                    else:
                        dp[i][j][k] = max(prices[i] + dp[i+1][0][k-1], dp[i+1][1][k])
        return dp[0][0][2]   #Here we are returning dp at n = 0 , j = 0 {buy} and k = 2 {max transactions} {since thats our requirement}