import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            dist = -(x * x + y * y)  # Negate to turn min-heap into max-heap
            heapq.heappush(max_heap, (dist, x, y))
            
            # Keep max-heap size <= k
            if len(max_heap) > k:
                heapq.heappop(max_heap) # Pops the largest (most distant) point
                
        return [[x, y] for dist, x, y in max_heap]