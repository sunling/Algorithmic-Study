from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid)==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0 
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=='1'):
                    count+=1
                    grid[i][j]='0'
                    self.bfs(grid,i,j)
        return count
    
    def bfs(self,grid,i,j): 
        queue = collections.deque()
        queue.append((i, j))  
        while queue: 
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            r,c = queue.popleft()  
            for d in directions:
                nr,nc = r+d[0],c+d[1]
                if self.is_valid(grid,nr,nc) and grid[nr][nc]=='1':
                    queue.append((nr,nc))
                    grid[nr][nc]='0'
            
    def is_valid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

    def printGrid(self, grid):
        for row in grid:
            print(row)

sol = Solution()
grid = [list(string) for string in ('11000', '11000', '00100', '00011')]
count = sol.numIslands(grid)
print(count)
