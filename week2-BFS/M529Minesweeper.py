from typing import List
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        if board[click[0]][click[1]] == "M": board[click[0]][click[1]] = "X"
        dir = [1,0], [0,1], [-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]
        q = deque()
        q.append(click)
        seen = set(click)
        
        def numBombsTangent(board, i, j):
            count = 0 
            for x, y in dir: 
                if 0 <= i + x < R and 0 <= j + y < C and board[i+x][y+j] == "M": count += 1 
            return count 

        while q: 
            for tup in range(len(q)):
                x, y = q.popleft()
                if board[x][y] == "E":
                    bombsNextTo = numBombsTangent(board, x, y)
                    board[x][y] = "B" if bombsNextTo == 0 else str(bombsNextTo)
                    if bombsNextTo == 0:
                        for a, b in dir:
                            if 0 <= a + x < R and 0 <= b + y < C and (a+x,b+y) not in seen:
                                q.append((a+x, b+y))
                                seen.add((a+x, b+y))
        return board 

sol = Solution()

input = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

print(sol.updateBoard(input,(3,0)))
        
