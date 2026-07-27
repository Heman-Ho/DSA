import heapq
class KthLargest:
    # Since we only have method for add, not delete, we only need to keep track of the current k largest elements
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        # Case 2: len of heap < k
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        # Case 3: len of heap == k
        else:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
            return self.heap[0]
