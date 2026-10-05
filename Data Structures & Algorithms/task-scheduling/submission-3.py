import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counts = Counter(tasks)
        max_heap = [(-count, task) for task, count in counts.items()]
        heapq.heapify(max_heap)
        
        q = deque()

        # X X Y Y, n = 2
        # heap: 
        # q: ((2, 1, X), (3, 1, Y))
        while max_heap or q:
            if not max_heap:
                time = q[0][0]

            if q and time == q[0][0]:
                _, neg_count, task = q.popleft()
                heapq.heappush(max_heap, (neg_count, task))

            neg_count, task = heapq.heappop(max_heap)
            if neg_count != -1:
                q.append((time + n + 1, neg_count + 1, task))
            time += 1
        
        return time