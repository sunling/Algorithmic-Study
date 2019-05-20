from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = []
        cols = set()  # 所有Q占的列的位置
        diag = set()  # 所有Q占的正斜对角的位置
        off_diag = set()  # 所有Q占的反斜对角的位置
        backtrack(0)

        def backtrack(i):
            if i == n:
                res.append(list(board))
            for j in range(n):
                if j not in cols and j-i not in diag and j+i not in off_diag:
                    cols.add(j)
                    diag.add(j-i)
                    off_diag.add(j+i)
                    board.append("."*(j)+"Q"+"."*(n-j-1))
                    backtrack(i+1)
                    board.pop()
                    off_diag.remove(j+i)
                    diag.remove(j-i)
                    cols.remove(j)

        return res


g = Solution()
print(g.solveNQueens(4))
