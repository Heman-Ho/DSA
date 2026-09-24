import heapq


class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half (values negated)
        # min_heap stores the larger half
        # Invariant: len(max_heap) == len(min_heap) OR len(max_heap) == len(min_heap) + 1
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 1. Route num through max_heap to min_heap to preserve order invariant
        val = -heapq.heappushpop(self.max_heap, -num)
        heapq.heappush(self.min_heap, val)

        # 2. Maintain size invariant: max_heap holds the extra element if count is odd
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0