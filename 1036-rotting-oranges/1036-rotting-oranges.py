import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1, 0), (0,1), (0, -1)]
        queue = collections.deque()
        freshoranges = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    freshoranges += 1
                
        # Basic checks
        if freshoranges == 0:
            return 0

        if not queue:
            return -1

        # minutes = -1
        max_minutes = -1
        while queue:
            # size = len(queue)
            x, y, m = queue.popleft()
            max_minutes = max(max_minutes, m)
            # size -= 1
            # m += 1
            for dx, dy in directions:
                i, j = x + dx, y + dy
                if 0 <= i <len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    grid[i][j] = 2
                    freshoranges -= 1
                    queue.append((i, j, m + 1))

        

        if freshoranges == 0:
            return max_minutes
        else:
            return -1


    
            
            



                
                


            
                    



                    # count = bfs(grid, i, j)
                    # print(count)
        




        # def bfs(grid, i, j):
        #     count = 0
        #     queue = deque([(i, j)])

        #     while queue:
        #         x, y = queue.popleft()
        #         if (0 <= x < len(grid)) and (0 <= y < len(grid[0])) and grid[x][y] == 1:
        #             grid[x][y] = 2
        #             for dx, dy in directions:
        #                 queue.append(grid, x + dx , y + dy)
        #             count += 1

        #     return count

        
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1:
                    return -1
        
        return count







        