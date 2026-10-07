import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        # use dijkstra's algorithm to find the shortest path to each node from k
        # Let distances[i] represent the shortest distance found from src to node i (initialy inf)
        distances = [float('inf')] * (n + 1)
        distances[0] = distances[k] = 0

        # initialize a min heap that holds a tuple (distance-from-src, node)
        # The min heap initially holds (0, k)
        min_heap = [(0, k)]

        # While the heap has nodes to be processed
        while min_heap:
            # dst, cur_node = pop from the min heap
            dst, cur_node = heapq.heappop(min_heap)
            
            # if dst > distances[cur_node] then continue because we already tried a shorter path
            if dst > distances[cur_node]:
                continue
            
            for neighbor, time in adj[cur_node]:
                new_dst = dst + time
                if new_dst < distances[neighbor]:
                    distances[neighbor] = new_dst
                    heapq.heappush(min_heap, (new_dst, neighbor))
        

        return -1 if max(distances) == float('inf') else max(distances)
