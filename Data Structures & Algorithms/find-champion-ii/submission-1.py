class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker = set(v for u, v in edges)

        res = -1
        for node in range(n):
            if node not in weaker:
                if res != -1:
                    return -1
                res = node
        
        return res