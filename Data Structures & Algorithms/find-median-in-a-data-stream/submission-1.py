class MedianFinder:

    def __init__(self):
        # Invariant: the data in the smaller half  of the sorted stream should be in the max heap
        #            and the data in the larger half of the sorted stream should be in the min heap
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # case 1: empty min heap
        if not self.min_heap:
            self.min_heap.append(num)
        # case 2: smaller than min_heap [0]
        elif num <= self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)

            if len(self.max_heap) >= 2 + len(self.min_heap):
                num = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -num)

        # case 2: num > min_heap[0]
        else:
            heapq.heappush(self.min_heap, num)

            if len(self.min_heap) >= 2 + len(self.max_heap):
                num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if not self.min_heap and not self.max_heap:
            return 0
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        
        return (self.min_heap[0] - self.max_heap[0]) / 2
        
        