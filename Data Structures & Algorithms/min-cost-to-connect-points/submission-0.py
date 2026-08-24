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
        edges = [] # holds (node_i, node_j, edge_weight)
        for i, [xi, yi] in enumerate(points):
            for j, [xj, yj] in enumerate(points):
                manhatten_distance = abs(xi - xj) + abs(yi - yj)
                if manhatten_distance != 0:
                    edges.append((i, j, manhatten_distance))
           
        MST = UnionFind(len(points))

        # We need to create a MST of all the nodes
        # 1. sort edges in ascending order by edge weight
        edges.sort(key=lambda x: x[2])
        res = 0

        # for all edges:
        for u, v, weight in edges:
            # 1. If adding the edge to our MST doesn't cause a cycle, add it (Use union find data structure)
            if MST.union(u, v):
                res += weight

        return res
        