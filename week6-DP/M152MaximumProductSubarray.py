from typing import List

Input: [2, 3, -2, 4]
Output: 6


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n*big, n*small), min(n, n*big, n*small)
            maximum = max(maximum, big)
        return maximum


g = Solution()
print(g.maxProduct([-4, -3, -2]))

# Runtime: 40 ms, faster than 97.85 % of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 13.1 MB, less than 90.12 % of Python3 online submissions for Maximum Product Subarray.
