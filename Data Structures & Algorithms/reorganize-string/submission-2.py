import heapq
from collections import defaultdict, Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        counts = Counter(s)

        max_heap = [(-count, c) for c, count in counts.items()]
        heapq.heapify(max_heap)

        # create a priority queue for the next letter to add
        # greedily choose the highest freq count letter 
        buffer = (1, "#")

        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
        
            if buffer[0] < 0:
                heapq.heappush(max_heap, buffer)
            buffer = (count+1, char)

        if len(res) == len(s):
            return "".join(res)
        else:
            return ""