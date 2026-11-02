import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        if not enough bricks => must use a ladder
        tentatively use ladders for each positive jump and push to a min heap 
        if we run out of ladders, replace the smallest jumped ladder with bricks
        """

        min_heap = [] 

        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]:
                continue
            heapq.heappush(min_heap, heights[i] - heights[i-1]) 
            if len(min_heap) > ladders:
                bricks_needed = heapq.heappop(min_heap)
                if bricks < bricks_needed:
                    return i - 1
                bricks -= bricks_needed
        
        return len(heights) - 1
                
