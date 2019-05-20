from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, temp, res):
        if len(temp) == len(nums):
            res.append(temp)
        for i in range(0, len(nums)):
            if nums[i] in temp:
                continue
            self.dfs(nums, temp + [nums[i]], res)


g = Solution()
input = [1, 2, 3]
print(g.permute(input))
