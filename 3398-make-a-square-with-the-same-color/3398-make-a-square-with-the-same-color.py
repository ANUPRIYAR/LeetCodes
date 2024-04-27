class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:      
        colormap = {'B':0 , 'W': 0}
        for i in range(2):
            for j in range(2):
                colormap[grid[i][j]] = colormap.get(grid[i][j], 0) + 1
                if colormap['B'] <= 2 or colormap['W'] <= 2:
                    if self.shift_matrix(grid, i, j):
                        return True
        return False


    def shift_matrix(self,grid,  i, j):
        colormap = {'B':0 , 'W': 0}
        for si in range(2):
            for sj in range(2):
                colormap[grid[i+ si][j +sj]] = colormap.get(grid[i+ si][j +sj], 0) + 1
        if colormap['B'] >2 or colormap['W'] > 2:
            return True
        return False