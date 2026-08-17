import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        counts = {}

        for c in s:
            if c in counts:
                counts[c][0] -= 1
            else:
                counts[c] = [-1, c]
        
        max_heap = []
        for value in counts.values():
            max_heap.append(value)
        heapq.heapify(max_heap)

        # create a priority queue for the next letter to add
        # greedily choose the highest freq count letter 
        buffer = [1, "#"]
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
        
            if buffer[0] < 0:
                heapq.heappush(max_heap, buffer)
            buffer = [count+1, char]

        if len(res) == len(s):
            return "".join(res)
        else:
            return ""