class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        n = len(coins)
        prev = [0 for _ in range(amount + 1)]
        cur = [0 for _ in range(amount + 1)]

        for j in range(amount + 1):
            if j % coins[0] == 0:
                prev[j] = j//coins[0]
            else:
               prev[j] = math.inf

        for i in range(1, n):
            for j in range(1, amount+1):
                notpick = prev[j]
                pick = math.inf
                if coins[i] <= j:
                    pick = 1 + cur[j-coins[i]]
                cur[j] = min(pick, notpick)
            prev = cur

        return prev[amount] if prev[amount] != math.inf else -1