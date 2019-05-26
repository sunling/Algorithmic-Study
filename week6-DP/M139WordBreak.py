from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
            
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i+1 - len(w) :i+1] and (dp[i - len(w)] or i - len(w) == -1):
                    dp[i] = True
        return dp[-1]

g = Solution()
print(g.wordBreak("applepenapple", ["apple", "pen"]))
                    
#Runtime: 36 ms, faster than 98.20 % of
# Python3 online submissions for Word Break.
