import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-count, letter) for letter, count in counts.items()]
        heapq.heapify(max_heap)

        res = []
        prev = None
        while max_heap:
            neg_count, letter = heapq.heappop(max_heap)
            res.append(letter)

            if prev is not None:
                heapq.heappush(max_heap, prev)

            if neg_count < -1:
                prev = (neg_count + 1, letter)
            else:
                prev = None
        
        return "".join(res) if len(res) == len(s) else ""
