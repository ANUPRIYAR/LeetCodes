from collections import deque
class Solution:
    # We can use Bfs Traversal to get the distance to nearest 0 (cant use dfs)
    # because bfs goes level by lebel , and in matrix the next level is surrounding 4 nodes 
    # In the queue, we add extra parmeter called d, which will be 0 for initial node 
    # and then d + 1 for subsequent, then as soon as we find popped node as 0 we return its d value
    # why are we doing d+ 1 beacuse , for each elevel until we find 0 , we keep increasing d by 1 
    # indicating 1 for 1 level
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # def find_distance(mat, i, j):
        #     directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        #     visited = {}

        #     queue = deque([(i,j,0)])
        #     while queue:
        #         x, y, d = queue.popleft()
        #         visited[(x,y)] = True

        #         # if value at x, y is 0, the return d
                # if mat[x][y] == 0:
                #     return d
        #         for dx, dy in directions:
        #             # check validity and if not visited
        #             if 0 <= x + dx < len(mat) and 0 <= y + dy < len(mat[0]) and (x + dx, y + dy) not in visited:
        #                 queue.append((x + dx,y + dy, d + 1 ))  # at every level we are adding 1 to d

        #     return -1

        # Traverse through matrix 
        ans = []
        visit = [[0 for _ in range(len(mat[0]))]for _ in range(len(mat))]
        dist = [[0 for _ in range(len(mat[0]))]for _ in range(len(mat))]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:  # we are getting the positions of zero cells , 
                    queue.append((i, j, 0))   # becoz we want only that to calculate distance of pther cells
                    visit[i][j] = 1         
                else:
                    visit[i][j] = 0


        directions = [(1, 0), (-1,0), (0,1), (0,-1)]

        while queue:
            x, y, d = queue.popleft()
            dist[x][y] = d

            for dx, dy in directions:
                # check validity and if not visited
                if 0 <= x + dx < len(mat) and 0 <= y + dy < len(mat[0]) and visit[x + dx][y + dy] == 0:
                    # so if the corrodinates are something we have not visited, and so the first one 
                    # would be at a distance 1 from popped element , we consider that d , and then at each subsequent
                    # levels keep adding 1
                    visit[x+dx][y+dy]= 1
                    queue.append((x + dx, y + dy, d + 1 )) 

        return dist



                    
                    
        #     ans.append(cols)
        # return ans