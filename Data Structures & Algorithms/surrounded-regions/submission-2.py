class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(board), len(board[0])

        q = deque()
        safe = set()

        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    if board[row][col] == "O":
                        q.append((row,col))
                        safe.add((row, col))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in safe and
                        board[nr][nc] == "O"
                    ):
                        q.append((nr, nc))
                        safe.add((nr,nc))


        for row in range(rows):
            for col in range(cols):
                if (row, col) not in safe:
                    board[row][col] = "X"