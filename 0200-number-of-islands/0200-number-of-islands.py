from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        def bfs(grid, i, j):
            queue = deque([(i, j)])

            while queue:
                (x, y) = queue.popleft()
                
                if 0 <= x < len(grid) and 0 <=  y < len(grid[0]) and grid[x][y] == "1":
                    grid[x][y] = "0"
                    for dx, dy in directions:
                        queue.append((x + dx, y + dy))

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands  += 1
                    bfs(grid, i, j)

        return islands
