class UnionFind():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i == parent_j:
            return False # cycle detected
        
        # smaller tree under bigger tree (make i the smaller tree
        if self.size[parent_i] > self.size[parent_j]:
            parent_i, parent_j = parent_j, parent_i
        
        self.parents[parent_i] = parent_j
        self.size[parent_j] += self.size[parent_i]
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # exactly n - 1 edges 
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        
        return True