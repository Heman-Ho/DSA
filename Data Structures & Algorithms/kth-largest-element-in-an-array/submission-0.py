import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min heap of size K
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # we add every element one by one to the min heap
        for i in range(k, len(nums)):
            # add next element
            heapq.heappush(min_heap, nums[i])
            # Remove min element
            heapq.heappop(min_heap)
        
        return heapq.heappop(min_heap)

            