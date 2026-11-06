class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.curword = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                visited = set()
                if self.backtrack(board, self.curword, word, i, j, visited):
                    return True
        return False
    
    def backtrack(self, board, curword, word, i, j, visited):
        
        if len(self.curword) == len(word):
            return True

        if len(self.curword) > len(word):
            return False
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False 
        
        if board[i][j] != word[len(self.curword)]:
            return False
        
        if (i,j) in visited:
            return False
        
        self.curword.append(board[i][j])
        visited.add((i,j))

        if len(self.curword) == len(word):
            return True

        found = (
            self.backtrack(board, self.curword, word, i + 1, j, visited) or
            self.backtrack(board, self.curword, word, i - 1, j, visited) or
            self.backtrack(board, self.curword, word, i, j + 1, visited) or
            self.backtrack(board, self.curword, word, i, j - 1, visited)
        )

        self.curword.pop()
        visited.remove((i,j))
        return found


        