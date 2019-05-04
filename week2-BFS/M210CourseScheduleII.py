from typing import List  
from collections import deque,defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {i:set() for i in range(numCourses)}
        neigh = defaultdict(set)

        for i,j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        
        queue = deque([i for i in dic if not dic[i]])
        count, res = 0,[]
        while queue:
            node = queue.popleft()
            res.append(node)
            count+=1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []


    

numCourses = 4
p = [[1,0],[2,0],[3,1],[3,2]]
p1 = [[1,0],[2,0],[0,1],[0,2]]
p2 = [[1,3],[2,3],[0,1],[0,2]]

sol = Solution()
print(sol.findOrder(numCourses,p2))