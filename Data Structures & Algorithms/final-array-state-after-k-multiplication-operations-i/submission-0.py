import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(num, i) for i, num in enumerate(nums)] # stores list of (val, index)
        heapq.heapify(min_heap)

        for _ in range(k):
            val, i = heapq.heappop(min_heap)
            nums[i] = val * multiplier
            heapq.heappush(min_heap, (val * multiplier, i))
        
        return nums
