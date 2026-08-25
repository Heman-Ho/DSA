from collections import defaultdict
import heapq
from typing import List


class Solution:

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        # min_stops[node] records the fewest stops used to reach 'node' so far
        min_stops = [float("inf")] * n

        # min_heap: (cost, stops_used_to_reach_node, node)
        min_heap = [(0, 0, src)]

        while min_heap:
            cost, stops, u = heapq.heappop(min_heap)

            # First time we pop dst, it is guaranteed to be the cheapest valid path
            if u == dst:
                return cost

            # Pruning 1: If we have already reached 'u' with <= stops, prune this branch
            if stops >= min_stops[u]:
                continue
            min_stops[u] = stops

            # Pruning 2: If we are at k stops, moving forward uses k+1 stops (exceeds limit)
            # Note: k stops between src and dst means at most k + 1 flights (edges)
            if stops > k:
                continue

            for v, price in adj[u]:
                heapq.heappush(min_heap, (cost + price, stops + 1, v))

        return -1