from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        degrees = [0] * n
        adj = defaultdict(set)

        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            adj[u].add(v)
            adj[v].add(u)
        
        q = deque()
        for node in range(n):
            if degrees[node] == 1:
                q.append(node)
                
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in adj[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        q.append(neighbor)
        return list(q)


