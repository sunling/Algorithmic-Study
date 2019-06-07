from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)

        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        #将没有prerequisite的课程先全部放到stack里
        stack = [n for n in range(numCourses) if not graph[n]]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            for n in neighbors[node]:
                graph[n].remove(node)
                if not graph[n]:
                    stack.append(n)
        return count == numCourses
    
# Runtime: 48 ms, faster than 86.16 % of Python3 online submissions
# for Course Schedule.



