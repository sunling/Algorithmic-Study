class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 0 ≤ n ≤ 500
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxC = 0
        for i in range(len(nums)):
            # current num
            # burst current Balloon, to get how man
            # 爆破当前气球得到多少coin
            currC = nums[i]
            if i - 1 > 0:
                currC *= nums[i - 1]
            if i + 1 < len(nums):
                currC *= nums[i + 1]

                # left
                # right
    def helper(nums, res):
