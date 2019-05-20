from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, m, n, i, j, word):
                    return True
        return False

    def dfs(self, board, m, n, i, j, word):
        if not word:
            return True
        if 0 <= i < m and 0 <= j < n and board[i][j] == word[0]:
            c = board[i][j]
            board[i][j] = '*' 
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]: 
                if self.dfs(board, m, n, x, y, word[1:]):
                    board[i][j] = c
                    return True
            board[i][j] = c 
        return False


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(s.exist(board, 'ABCCED'))
