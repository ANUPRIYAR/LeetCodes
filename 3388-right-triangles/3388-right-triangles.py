class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        row_count = {}
        rowcount, colcount = [0]* rows, [0]* cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowcount[i] += 1
                    colcount[j] += 1
        triangles = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    triangles += (rowcount[i] - 1)* (colcount[j]- 1)
        return triangles
                    
                    
                    

                    
                    
                        
        