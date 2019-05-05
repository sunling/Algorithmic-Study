
# 776. Strobogrammatic Number II
# https: // www.lintcode.com/problem/strobogrammatic-number-ii/description

from collections import deque


class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """

    def findStrobogrammatic(self, n):
        # write your code here
        res = self.find(n, n)
        return res

    def find(self, m, n):
        if m == 0:
            return []
        if m == 1:
            return ["0", "1", "8"]

        res = self.find(m - 2, n)
        for a in res:
            if m != n:
                res.append("0" + a + "0")

            res.append("1" + a + "1")
            res.append("8" + a + "8")
            res.append("6" + a + "9")
            res.append("9" + a + "6")

        return res

g = Solution()
print(g.findStrobogrammatic(3))
