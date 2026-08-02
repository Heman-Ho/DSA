class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n
        
        def find(self, i):
            # flatten the tree if possible while finding root
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

        def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)
            if root_i == root_j:
                # Cycle was detected => return False
                return False
            # We want the larger rank tree to be the new root
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            # update the rank if connecting the sets creates a larger tree
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            return True
            
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dsu = self.UnionFind(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return True


        