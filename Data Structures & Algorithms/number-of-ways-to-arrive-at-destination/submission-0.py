from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        min_heap = [(0, 0)]    # (distance, node)

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                cand = d + w
                if cand < dist[v]:
                    dist[v] = cand
                    ways[v] = ways[u]
                    heapq.heappush(min_heap, (cand, v))
                elif cand == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1]