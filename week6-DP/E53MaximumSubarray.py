from typing import List

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums 
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])  
        return max(dp)

g = Solution()
print(g.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Runtime: 40 ms, faster than 97.12 % of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.7 MB, less than 37.70 % of Python3 online submissions for Maximum Subarray.
