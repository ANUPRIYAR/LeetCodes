class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        if not M:
            return 0

        n = len(M)

        # Convert matrix into graph
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visit = [False]* n

        # write dfs function
        def dfs(u):
            for v in graph[u]:
                if visit[v] == False:
                    visit[v] = True
                    dfs(v)

        
        # count the non-connected nodes
        count = 0

        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)

        return count




