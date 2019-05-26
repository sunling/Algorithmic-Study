from typing import List
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        minP, maxProfit = float('Inf'), 0
        for p in prices:
            if p < minP:
                minP = p
            maxProfit = max(maxProfit, p - minP)
        return maxProfit


input =  [7, 1, 5, 3, 6, 4]
g = Solution()
print(g.maxProfit(input))

# Runtime: 40ms, fasterthan95.50 % of
# Python3 online submissions for Best Time to Buy and Sell Stock.
