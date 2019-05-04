from typing import List
from collections import deque,defaultdict
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        #超时 待优化
        # queue = deque([(src,0,-1)]) 
        # finalP = -1  
        # while queue:
        #     cityno,price,stop = queue.popleft() 
        #     if cityno == dst and stop<=K:  
        #         if finalP == -1 or finalP > price:
        #             finalP = price 
        #     for flight in flights:
        #             if cityno == flight[0]:
        #                 queue.append((flight[1], price+flight[2],stop+1))   
        # return finalP

        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heappush(heap, (p + f[i][j], j, k - 1))
        return -1

sol = Solution()
print(sol.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))


                    
                    

                




