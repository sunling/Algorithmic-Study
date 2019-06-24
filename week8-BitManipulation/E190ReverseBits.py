class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            print(ans)
            n >>= 1
        return ans


g = Solution()
print(g.reverseBits(6))
