from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Run Dijkstra's algorithm starting from node k
        adj = defaultdict(set)
        for u, v, time in times:
            adj[u].add((time, v))

        min_heap = [(0, k)] # holds (time it takes to reach node, node)
        min_times = [float('inf')] * (n+1)
        min_times[k] = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > min_times[node]:
                continue
           
            for neighbor in adj[node]:
                if neighbor[0] + time < min_times[neighbor[1]]:
                    min_times[neighbor[1]] = neighbor[0] + time
                    heapq.heappush(min_heap, (time + neighbor[0], neighbor[1]))
     
        farthest = max(min_times[1:])
        if farthest == float('inf'):
            return -1
        else:
            return farthest

        # return the max time of all the nodes or -1 if time == inf