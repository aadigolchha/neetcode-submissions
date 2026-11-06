class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.visited = set()
        self.count = 0
        rows, cols = len(grid), len(grid[0])


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.count += 1 
                    self.dfs(grid, self.visited, row, col)

        return self.count

    def dfs(self, grid, visited, r, c):
        
        rows, cols = len(grid), len(grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
            return 

        if grid[r][c] == "0":
            return 

        visited.add((r,c))

        for neighbor in [0,1], [0, -1], [1, 0], [-1, 0]:
            new_r, new_c = r + neighbor[0], c + neighbor[1]
            self.dfs(grid, visited, new_r, new_c)
            
        
        
 
                
        
            
