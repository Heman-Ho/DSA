class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i]) # we are flattening the union find tree
        return self.parents[i]
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return False

        self.parents[parent_j] = parent_i
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Construct a graph where each node is a point 
        # There is an edge between every 2 nodes
        n = len(points)
        edges = [] # holds (node_i, node_j, edge_weight)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((i, j, dist))
           
        MST = UnionFind(n)

        # We need to create a MST of all the nodes
        # 1. sort edges in ascending order by edge weight
        edges.sort(key=lambda x: x[2])
        res = 0
        num_nodes = 0

        # for all edges:
        for u, v, weight in edges:
            # If adding the edge to our MST doesn't cause a cycle, add it (Use union find data structure)
            if MST.union(u, v):
                res += weight
                num_nodes += 1
            # If our MST has n - 1 nodes, then the graph is complete
            if num_nodes == n - 1:
                return res
        return res

        