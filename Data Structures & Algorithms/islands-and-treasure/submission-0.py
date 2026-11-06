class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < len(grid) and 
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] == 2147483647
                ): 
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        
        