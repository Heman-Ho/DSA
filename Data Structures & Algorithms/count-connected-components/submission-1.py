from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Construct an adjacency list from the edges
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        stack = []
        visited = set()
        res = 0

        while len(visited) != n:
            for node in range(n):
                if node not in visited:
                    stack.append(node)
                    res += 1
                    break
            
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in adj[node]:
                    stack.append(neighbor)
        return res
