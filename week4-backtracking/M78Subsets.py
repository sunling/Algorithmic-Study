class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

    def dfs(self, nums, start, end, path, res):
        