import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(len(points)):
            xi, yi = points[i]
            distance = math.sqrt(xi * xi + yi * yi)
            min_heap.append((distance, points[i]))
        
        heapq.heapify(min_heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
        
        
