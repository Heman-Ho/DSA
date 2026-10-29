class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))
        
        res = 0
        seen = set()
        stack = [0]

        while stack:
            node = stack.pop()
            seen.add(node)
            for neighbor, cost in adj[node]:
                if neighbor in seen:
                    continue
                stack.append(neighbor)
                res += cost
        
        return res
    

        
