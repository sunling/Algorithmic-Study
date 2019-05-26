
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float("Inf")] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1) :
            dp[i][0] = i
        for j in range(n + 1) :
            dp[0][j] = j
        
        print(dp)
        for i in range(1, m + 1) :
            for j in range(1, n + 1) :
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    
        return dp[-1][-1]
                
g = Solution()
print(g.minDistance("horse", "ros"))

# Runtime: 180ms,
# faster than 80.08 % of Python3 online submissions for Edit Distance.
            
            
