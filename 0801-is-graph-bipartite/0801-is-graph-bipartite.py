class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node):
            visited.add(node)

            # Traverse for all children of the node
            for child in graph[node]:
                if child not in visited:
                    colors[child] = not colors[node]
                    dfs(child)
                else:
                    if colors[child] == colors[node]:
                        self.BiPart = False

        visited, colors = set(), [False for _ in range(len(graph))]
        self.BiPart = True

        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
                
        return self.BiPart