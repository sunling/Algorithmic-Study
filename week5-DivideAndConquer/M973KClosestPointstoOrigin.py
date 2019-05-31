import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for a, b in points:
            d = a ** 2 + b ** 2
            heapq.heappush(heap, (-d, a, b))
            if len(heap) > K:
                heapq.heappop(heap)
        return [[a, b] for d, a, b in heap]
        
            
# Runtime: 380 ms, faster than 63.37 % of
# Python3 online submissions for K Closest Points to Origin.
