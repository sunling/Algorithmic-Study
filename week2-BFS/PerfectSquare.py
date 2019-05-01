from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        queue = deque([(n,1)])
        res = 1
        while queue: 
            num,res = queue.popleft()
            for square in squares:
                if square == num:
                    return res
                if num < square:
                    break
                queue.append((num-square,res+1)) 

sol = Solution()
print(sol.numSquares(14))