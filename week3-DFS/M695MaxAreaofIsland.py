
from typing import List

# Given a non-empty 2D array grid of 0's and 1's,
# an island is a group of 1's(representing land)
# connected 4-directionally(horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # 14.68%
        # if not grid or not grid[0]:
        #     return 0
        # m, n = len(grid), len(grid[0])
        # visited = set()

        # def dfs(grid, m, n, i, j, area):
        #     if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited:
        #         return area
        #     visited.add((i, j))
        #     if grid[i][j] == 1:
        #         area += 1
        #         for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
        #             area = max(area, dfs(grid, m, n, x, y, area))
        #     return area
        # maxArea = 0
        # for i in range(m):
        #     for j in range(n):
        #         area = dfs(grid, m, n, i, j, 0)
        #         maxArea = max(maxArea, area)
        # return maxArea

        # 112 ms 45.16%
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            area = 1
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                    area += dfs(x, y)
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea


g = Solution()
grid = [[0, 0, 1, 0, 1, 1, 0, 0]]

print(g.maxAreaOfIsland(grid))
