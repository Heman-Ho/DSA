class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
        
        def find(self, i):
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i]) # We compress the tree while finding the root 
            return self.parent[i]

        def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)
            if root_i == root_j:
                # We detected a cycle
                return False
            self.parent[root_i] = root_j
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = self.UnionFind(len(edges))
        # iterate through the edges, adding it to a new graph
        for node1, node2 in edges:
            # if adding the edge creates a cycle, then we return that edge
            if not graph.union(node1-1, node2-1):
                return [node1, node2]

       
        # It is guaranteed to be the answer that appears last in the input edges because
        # we are iterating throught edges from start to end

        
        