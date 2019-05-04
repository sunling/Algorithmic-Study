from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <3 or len(board[0]) < 3:
            return
        m, n = len(board), len(board[0])

        #for the first row and last row
        for j in range(n):
            for i in 0,m-1:
                if board[i][j] == 'O':
                    self.bfs(board,i,j,m,n)
        #for the first column and last column 
        for i in range(1,m-1):
            for j in 0,n-1:
                if board[i][j] == 'O':
                    self.bfs(board,i,j,m,n)
        
        #O-X G-O
        for row in board:
            for j in range(n):
                if row[j] != 'X':
                    row[j] = 'X' if row[j] == 'O' else 'O'

    def bfs(self,board, i, j, m, n):
        queue = deque([(i,j)])
        board[i][j] = 'G'
        while queue:
            currx,curry = queue.popleft() 
            for di,dj in [[1, 0], [-1, 1], [-1, -1], [1, -1]]:
                currx+=di
                curry+=dj
                if 0 <= currx < m and 0 <= curry < n and board[currx][curry] == 'O':
                    queue.append((currx,curry))
                    board[currx][curry] = 'G'

sol = Solution()
input = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(input)
print(input)
        

        