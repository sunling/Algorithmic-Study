from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # 存储Q在每一行放的位置，index代表行，data代表Q放在第几列
        # 例如cols = [1,3,0,2], 第一行的话Q在第二个位置
        cols = [-1] * n
        self.dfs(n, cols, 0, [], res)
        return res

    def dfs(self, n, cols, currR, board, res):
        if currR == n:
            res.append(list(board))
            return
        for j in range(n):
            # 更新当前行的Q的列位置
            cols[currR] = j
            if self.is_valid(cols, currR):
                board.append("."*(j)+"Q"+"."*(n-j-1))
                self.dfs(n, cols, currR + 1, board, res)
                board.pop()

    # 针对当前行currR, Q新放的位置cols[currR]是否有效
    def is_valid(self, cols, currR):
        for r in range(currR):
            if cols[r] == cols[currR] or abs(cols[r] - cols[currR]) == currR - r:
                return False
        return True


g = Solution()
print(g.solveNQueens(4))
