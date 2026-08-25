from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # represent the problem as a graph with courses as nodes and 
        # an edge from course a to course b if a is a prereq of b
        # return false if there is a cycle

        # perform a topological sort
        adj = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for a, b in prerequisites:
            # you must take b before you can take a
            adj[b].append(a)
            in_degrees[a] += 1
        
        q = deque() # holds valid courses that you can take
        for node, degree in enumerate(in_degrees):
            if degree == 0:
                q.append(node)
        
        num_taken = 0
        while q:
            node = q.popleft()
            num_taken += 1
            for neighbor in adj[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)
        
        return num_taken == numCourses
            