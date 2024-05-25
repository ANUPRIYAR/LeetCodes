class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]

        def dfs(image, sr, sc, old_color, color):
            if sr < 0 or sr >= len(image) or sc <0 or sc >= len(image[0]):
                return

            if image[sr][sc] == color:
                return 
            if image[sr][sc] != old_color:
                return 

            directions = [(1, 0), (-1, 0), (0, 1 ), (0, -1)]
            image[sr][sc] = color

            for dx, dy  in directions:
                dfs(image, sr + dx, sc + dy, old_color, color )


        dfs(image, sr, sc, old_color, color)
        return image