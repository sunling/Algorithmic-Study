class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        # path[i,j] = Number of paths from [i,j] to destination
        # path[m-1,n-1] = 1
        # return path[0,0]
        paths = [[-1] * n for _ in range(m)]
        paths[m - 1][n - 1] = 1
        return self.helper(m, n, 0, 0, paths)

    def helper(self, m, n, i, j, paths):
        if 0 <= i < m and 0 <= j < n:
            if paths[i][j] != -1:
                return paths[i][j]
            paths[i][j] = self.helper(m, n, i+1, j, paths) + \
                self.helper(m, n, i, j + 1, paths)
            return paths[i][j]
        return 0


g = Solution()
print(g.uniquePaths(3, 2))


# Exceed time limit
# def uniquePaths(self, m: int, n: int) -> int:
#     count = self.dfs(m, n, 0, 0)
#     return count

# def dfs(self, m, n, i, j):
#     print("---------------------")
#     print("i={},j={}".format(i, j))
#     if 0 <= i < m and 0 <= j < n:
#         if i == m - 1 and j == n - 1:
#             return 1
#         return self.dfs(m, n, i + 1, j) + self.dfs(m, n, i, j + 1)
#     return 0
