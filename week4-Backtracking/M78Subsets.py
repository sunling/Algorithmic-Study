from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, path, res):
        res.append(path)
        print("-------------------")
        print("res:{}".format(res))
        print("-------------------")
        print("dfs({}):{}".format(start, path))
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, path+[nums[i]], res)
            # path.pop()


g = Solution()
print(g.subsets([1, 2, 3]))
