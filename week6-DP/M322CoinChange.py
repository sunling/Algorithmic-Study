from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        coins.sort(reverse = True)
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return - 1 if dp[-1] == MAX else dp[-1]
        
g = Solution()
print(g.coinChange([1, 2, 5], 11))

# Runtime: 1008ms,
# faster than 80.28 % of Python3 online submissions for Coin Change.

# With coins.sort(reverse = True)
# Runtime: 996ms,
# faster than 80.93 % of Python3 online submissions for Coin Change.
