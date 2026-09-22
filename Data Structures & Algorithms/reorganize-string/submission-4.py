import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = []

        for s, count in counts.items():
            heap.append((-count, s))
        heapq.heapify(heap)

        prev = None
        res = []
    
        while heap:
            count, letter = heapq.heappop(heap)
            res.append(letter)
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count < -1:
                prev = (count+1, letter)
        
        if prev:
            return ""
        return "".join(res)