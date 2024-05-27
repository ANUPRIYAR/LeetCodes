class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:     
        # Checking if the nodes are either directed towards or in a cycle are not Safe Nodes
        def dfscycle(graph, node, vis, pathvis, check):
            vis[node] = 1
            pathvis[node] = 1

            for child in graph[node]:
                if vis[child] == 0:
                    if dfscycle(graph, child, vis, pathvis, check):
                        check[node] = 0
                        return True

                else:
                    if pathvis[child] == 1:
                        check[node] = 0
                        return True

            pathvis[node] = 0
            check[node] = 1
            return False

        vis = [0]*len(graph)
        pathvis = [0]*len(graph)
        check = [0]*len(graph)

        for i in range(len(graph)):
            if vis[i] == 0:
                dfscycle(graph, i , vis, pathvis, check)


        safenodes = [i for i in range(len(check)) if check[i] == 1]
        return safenodes