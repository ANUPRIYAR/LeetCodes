class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        k = float("inf")
        cost = [[k for _ in range(n)] for _ in range(n)]

        for u, v, w in edges:
            cost[u][v] = cost[v][u] = w

        for i in range(n):
            for j in range(n):
                if i==j:
                    cost[i][j] = 0


        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j] )



        ans = -1
        k = sys.maxsize
        d = {}
        for i in range(n):
            connecting_cities = 0
            for j in range(n):
                if i != j and cost[i][j] <= distanceThreshold:
                    connecting_cities += 1

            
            d[i] = connecting_cities   # storing how many connecting cities within the distance threshold
        m1 = min(d.values())
        m2 = 0
        for k, v in d.items():
            if m1 == v:
                m2 = max(m2, k)
        return m2
                # if count <= k:
                #     ans = i
                #     k = count   # we are finding the latest i and less than distanceThreshold

            # return ans

        







        