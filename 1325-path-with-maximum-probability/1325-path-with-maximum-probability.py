from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create adjacency list 
        adj = defaultdict(list)
        for i, nodes in enumerate(edges):
            print(nodes)
            u, v = nodes[0], nodes[1]
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        prob_list = [0]* n
        prob_list[start_node] = 1
        pq = []
        heapq.heappush(pq, (-1, start_node))

        while pq: 
            probability, node = heapq.heappop(pq) 

            if node == end_node:
                return -probability

            for neighbours in adj[node]:
                curnode = neighbours[0]
                curprob = neighbours[1]

                if -probability * curprob > prob_list[curnode]:
                    prob_list[curnode] = -probability * curprob
                    heapq.heappush(pq, (-prob_list[curnode], curnode))

        return 0


        



        

        