from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # b -> a 
        res = [] 

        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1
        
        q = deque()
        for course, deg in enumerate(in_degree):
            if deg == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            res.append(course)
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return [] if len(res) < numCourses else res
            