from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = [set() for i in range(numCourses)]
        post = [set() for i in range(numCourses)]

        for sec,fir in prerequisites:
            pres[sec].add(fir)
            post[fir].add(sec)
        #no idea


sol = Solution()
print(sol.canFinish(6, [[1, 0], [2, 1], [3, 1], [4, 3], [4, 2], [5, 2], [5, 3]]))