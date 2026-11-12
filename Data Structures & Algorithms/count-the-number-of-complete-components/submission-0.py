from collections import defaultdict, deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = [False] * n
        complete = 0

        for start in range(n):
            if seen[start]:
                continue
            # BFS this component, tally size and edge-degree sum
            q = deque([start])
            seen[start] = True
            size = 0
            deg_sum = 0
            while q:
                v = q.popleft()
                size += 1
                deg_sum += len(adj[v])
                for u in adj[v]:
                    if not seen[u]:
                        seen[u] = True
                        q.append(u)
            if deg_sum == size * (size - 1):
                complete += 1

        return complete