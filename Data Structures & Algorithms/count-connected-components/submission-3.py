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

        for i in range(n):
            if i not in visited:
                # We found a connected component
                visited.add(i)
                stack.append(i)
                res += 1
            
                # Run dfs on the new component, marking connected nodes as visited
                while stack:
                    node = stack.pop()
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)
        return res