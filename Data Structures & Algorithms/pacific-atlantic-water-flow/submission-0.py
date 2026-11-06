class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.heights = heights
        self.rows, self.cols = len(heights), len(heights[0])

        result = []

        for row in range(self.rows):
            for col in range(self.cols):
                self.visited = []
                self.reach_atlantic, self.reach_pacific = False, False
                height = heights[row][col]
                self.dfs(height, row, col)
                if self.reach_atlantic and self.reach_pacific:
                    result.append([row, col])
        return result



    def dfs(self, height, r, c):

        if (
            r < 0 or r >= self.rows or
            c < 0 or c >= self.cols or
            self.heights[r][c] > height or
            (r,c) in self.visited):
            return

        self.visited.append((r,c))

        if r == self.rows - 1 or c == self.cols - 1:
            self.reach_atlantic = True
        if r == 0 or c == 0:
            self.reach_pacific = True
        
        height = self.heights[r][c]

        self.dfs(height, r+1, c)
        self.dfs(height, r-1, c)
        self.dfs(height, r, c+1)
        self.dfs(height, r, c-1)




