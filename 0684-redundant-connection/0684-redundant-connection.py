from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # If we find an edge which connects two nodes , which were already connected , 
        # then we will get an edge which will form a cycle
        
        graph = defaultdict(list)
        # Lets start by constructing graph,see the 2 nodes we get is already connected or not
        # if not connected we will add the edges for the node in our graph
        for a, b in edges:
            if self.isalreadyconnected(graph, a, b):
                return [a, b]
            else:
                graph[a].append(b)
                graph[b].append(a)

        return None # since one of the constraints states : The given graph is connected.,
                    #  so we dont have to care about the else case  




    #  what we can do is, we will traverse through neighbours of node A, 
    # these neighbours are the ones before adding the edge for a, b so technically if 
    # there is no cyle , then it should not exist
    # and try to see we reach b, if we do, then its connected else not connected
    def isalreadyconnected(self, graph, a, b):
        visited = set()
        queue = deque([a])
        
        while queue:
            node = queue.popleft()
            if node == b:  # check if node obtained from q is b
                return True
            
            # add the node to visited to avoid visiting the already visited node
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
        
        # if after checking out all the neighbouring nodes ,
        #  we dont find node:b then return False
        return False



            




        

        

        