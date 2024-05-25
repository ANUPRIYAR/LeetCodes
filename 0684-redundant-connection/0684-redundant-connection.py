from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:       
        graph = defaultdict(list)

        # Logic exactly same as bfs , but bfs replaced with dfs traversal
        for a, b in edges:
            visited = set()  # we make a fresh visited because we call dfs for every pair of edges
            if self.isalreadyconnected(graph, visited, a, b):
                return [a, b]
            else:
                graph[a].append(b)
                graph[b].append(a)

        return None # since one of the constraints states : The given graph is connected.,
                    #  so we dont have to care about the else case  

    # dfs function to check if path exists between nodes a and b
    def isalreadyconnected(self, graph, visited, a, b):
        if a == b:
            return True

        # mark u as visited
        visited.add(a)

        # iterate through all the neighbors of u and if they are not visited call dfs on them
        for neighbour in graph[a]:
            if neighbour not in visited:

                # we have to reach b, so parent will be neigbour and child will be b
                if self.isalreadyconnected(graph, visited, neighbour, b):
                    return True
        return False