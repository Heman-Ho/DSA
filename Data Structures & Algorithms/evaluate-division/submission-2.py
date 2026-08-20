from collections import defaultdict
from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a graph: Nodes = all ai, bi in equations
        # create an edge ai -> bi with edge weight of the correspoding value for each ai, bi in equations
        # Also create an edge bi -> ai with 1/value edge weight

        # Run bfs on every query to see if ai can reach bi, while multiplying the edge weight
        graph = defaultdict(dict)
        for i, equation in enumerate(equations):
            u, v = equation[0], equation[1] 
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        
        res = []
       
        for start, target in queries:
            if start not in graph or target not in graph:
                res.append(-1.0)
                continue
            if start == target:
                res.append(1.0)
                continue

            q = deque() # Holds a tuple (cur_node, cur_product)
            q.append((start, 1))
            seen = {start}
            found = False
           
            while q and not found:
                u, cur_weight = q.popleft()
                for neighbor, weight in graph[u].items():
                    if neighbor in seen:
                        continue
                    if neighbor == target:
                        found = True
                        res.append(cur_weight * weight)
                        break
                    seen.add(neighbor)
                    q.append((neighbor, cur_weight * weight))

            if not found:
                res.append(-1.0)
        
        return res


        