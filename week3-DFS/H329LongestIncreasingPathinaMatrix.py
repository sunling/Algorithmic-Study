from typing import List

#Given an integer matrix, find the length of the longest increasing path.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0 
        m, n = len(matrix), len(matrix[0])
        #build array to store longest inc path for each element in the matrix
        res = [[0] * n for _ in range(m)]
        maxc = 1
        for i in range(m):
            for j in range(n):
                self.dfs(matrix, m, n, i, j, res)
                maxc = max(maxc, res[i][j])
            
        return maxc

    def dfs(self, matrix, m, n, i, j, res):
        if res[i][j] != 0:
            return
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                self.dfs(matrix, m, n, x, y,res)
                res[i][j] = max(res[i][j], res[x][y] + 1)

        if res[i][j] == 0:
            res[i][j] = 1
                
g = Solution()
nums = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print(g.longestIncreasingPath(nums))
