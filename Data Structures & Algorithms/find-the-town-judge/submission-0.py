from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # create a graph: nodes = people
        # directed edge a -> b if person a trusts person b
        adj = defaultdict(set)
        for edge in trust:
            adj[edge[0]].add(edge[1])
        
        # if more than one person has no out edges, return -1
        # if no person has 0 out edges, return -1
        if len(adj) != n - 1:
            return -1

        # Loop through nodes to determine the judge
        judge = 0
        for person in range(1, n+1):
            if person not in adj:
                judge = person
                break
        
        # loop through nodes to check if every person trusts the judge
        for person in range(1, n+1):
            if person == judge:
                continue
            if judge not in adj[person]:
                return -1

        return judge