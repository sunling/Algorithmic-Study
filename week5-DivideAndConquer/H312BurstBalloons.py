from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = [[0] * len(nums) for _ in nums]

        def burst(i, j):
            if cache[i][j]:
                return cache[i][j]
            coin = 0
            for k in range(i + 1, j):
                coin = max(coin, burst(i, k) +
                           nums[i] * nums[k] * nums[j] + burst(k, j))
                cache[i][j] = coin
            return coin
        return burst(0, len(nums)-1) 


g = Solution()
print(g.maxCoins([3, 1, 5, 8]))

# Runtime: 736 ms, faster than 24.07 % of 
# Python3 online submissions for Burst Balloons.
