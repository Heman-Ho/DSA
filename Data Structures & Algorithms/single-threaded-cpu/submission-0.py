import heapq
from typing import List


class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 1. Attach original index to each task and sort by enqueue time
        # Format: (enqueue_time, processing_time, original_index)
        indexed_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        indexed_tasks.sort()

        min_heap = []  # Stores: (processing_time, original_index)
        res = []
        t = 0
        i = 0
        n = len(tasks)

        while i < n or min_heap:
            # If CPU is idle and heap is empty, jump time forward to next arrival
            if not min_heap and t < indexed_tasks[i][0]:
                t = indexed_tasks[i][0]

            # Add all tasks that have arrived by current time t into min_heap
            while i < n and indexed_tasks[i][0] <= t:
                _, proc_time, idx = indexed_tasks[i]
                heapq.heappush(min_heap, (proc_time, idx))
                i += 1

            # Process one task (shortest proc_time, then smallest index)
            proc_time, idx = heapq.heappop(min_heap)
            t += proc_time
            res.append(idx)

        return res