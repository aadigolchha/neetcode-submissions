class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if self.backtrack(board, word, 0, r, c, set()):
                    return True

        return False

    def backtrack(self, board, word, index, r, c, visited):
        
        rows, cols = len(board), len(board[0])

        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            (r, c) in visited or
            board[r][c] != word[index]
        ):
            return False

        if index == len(word) - 1:
            return True

        visited.add((r, c))

        found = (
            self.backtrack(board, word, index + 1, r + 1, c, visited) or
            self.backtrack(board, word, index + 1, r - 1, c, visited) or
            self.backtrack(board, word, index + 1, r, c + 1, visited) or
            self.backtrack(board, word, index + 1, r, c - 1, visited)
        )

        visited.remove((r, c))

        return found