from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        min_heap = [count for count in counts.values()]
        heapq.heapify(min_heap)

        while k > 0:
            if min_heap[0] > k:
                return len(min_heap)
            else:
                k -= heapq.heappop(min_heap)

        return len(min_heap)
