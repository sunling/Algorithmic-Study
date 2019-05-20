from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        self.dfs(dic, digits, "", result)
        return result

    def dfs(self, d, digits, temp, res):
        if not digits:
            res.append(temp)
            return
        for letter in d[digits[0]]:
            self.dfs(d, digits[1:], temp+letter, res)


g = Solution()
print(g.letterCombinations('23'))
