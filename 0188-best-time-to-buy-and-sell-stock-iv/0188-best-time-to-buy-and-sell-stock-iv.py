class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        front = [[0 for _ in range(k + 1)] for _ in range(2)]
        cur = [[0 for _ in range(k + 1)] for _ in range(2)]

        for i in range(n-1, -1, -1):
            for k in range(1, k + 1):
                cur[0][k] = max(front[1][k] - prices[i] , front[0][k])
                cur[1][k] =  max(prices[i] + front[0][k-1] , front[1][k])
                front = cur.copy()

        return cur[0][k]