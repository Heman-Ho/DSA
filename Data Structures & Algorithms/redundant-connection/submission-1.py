class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i == parent_j:
            # cycle detected
            return False

        self.parents[parent_i] = parent_j
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = UnionFind(len(edges) + 1)
        for ai, bi in edges:
            if not graph.union(ai, bi): 
                return [ai, bi]