class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # find the in-degree of each node
        in_degrees = [0] * n

        for u, v in edges:
            in_degrees[v] += 1

        # if more than one node has an indegree of 0, return -1
        res = -1

        for i, deg in enumerate(in_degrees):
            if deg == 0:
                if res != -1:
                    return -1
                res = i
        
        return res
            