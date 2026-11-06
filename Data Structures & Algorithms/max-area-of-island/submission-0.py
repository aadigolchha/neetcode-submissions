class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.visited = set()
        largest = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    island_size = self.dfs(grid, row, col)
                    largest = max(largest, island_size)
        return largest

    def dfs(self, grid, row, col):

        if (
            row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or
            (row, col) in self.visited or grid[row][col] == 0
        ): return 0

        self.visited.add((row, col))

        connected = (
            self.dfs(grid, row + 1, col) +
            self.dfs(grid, row - 1, col) +
            self.dfs(grid, row, col + 1) +
            self.dfs(grid, row, col - 1) 
        )

        return 1 + connected
        

    
