class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.visited = set()
        self.count = 0
        rows, cols = len(grid), len(grid[0])


        for row in range(rows):
            for col in range(cols):
                self.count += self.dfs(grid, self.visited, row, col)

        return self.count

    def dfs(self, grid, visited, r, c):
        
        rows, cols = len(grid), len(grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
            return 0

        visited.add((r,c))
        
        if grid[r][c] == "0":
            return 0

        count = 0

        for neighbor in [0,1], [0, -1], [1, 0], [-1, 0]:
            new_r, new_c = r + neighbor[0], c + neighbor[1]
            count += self.dfs(grid, visited, new_r, new_c)

        self.count += 1
        return 1
            
        
        
 
                
        
            
