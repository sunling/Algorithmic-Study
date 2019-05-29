from typing import List

# Input: [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]: 
        #             dp[i] = max(dp[i], dp[j] + 1) 
        # return max(dp)

        # don't understand!!!
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            print(tails)
            print("size===={}".format(size))
            size = max(i + 1, size)
        return size


g = Solution()
print(g.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))

# Runtime: 1124ms, faster than 26.06 % of Python3
# online submissions for Longest Increasing Subsequence.
