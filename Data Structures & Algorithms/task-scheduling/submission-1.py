import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # At each cpu cycle, schedule the task that appears the most out remaining tasks, and is able to be used
        # Use a max heap that holds every task that is possible to schedule at the current cycle
        # Use a queue to hold tasks that are unable to cycle using a tuple (task_counts, time it's availabale again)
        cur_time = 0
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)
        queue = deque()
        
        while heap or queue:
            cur_time += 1

            # If a task becomes able to schedule, add to heap
            if queue and queue[0][1] <= cur_time:
                heapq.heappush(heap, queue[0][0])
                queue.popleft()

            # Case 1: There is no task able to schedule => stall
            if len(heap) == 0:
                continue
            
            # Case 2: schedule the task that has the highest freq and is avail
            count = heapq.heappop(heap)
            if count != -1:
                queue.append((count + 1, cur_time + n + 1))
        
        return cur_time
