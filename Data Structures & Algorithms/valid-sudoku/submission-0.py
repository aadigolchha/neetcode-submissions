class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = []

        for str in board:
            for char in str:
                if char in seen:
                    return False
                if char.isnumeric():
                    seen.append(char)
            seen.clear()

        for i in range(len(str)):
            for str in board:
                if str[i] in seen:
                    return False
                if str[i].isnumeric():
                    seen.append(str[i])
            seen.clear()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                small_grid = [board[i][j:j+3],
                            board[i+1][j:j+3],
                            board[i+2][j:j+3]]
                for k in range(0,3):
                    for l in range(0,3):
                        if small_grid[k][l] in seen:
                            return False
                        if small_grid[k][l].isnumeric():
                            seen.append(small_grid[k][l])
                seen.clear()
                small_grid.clear()
        
        return True




