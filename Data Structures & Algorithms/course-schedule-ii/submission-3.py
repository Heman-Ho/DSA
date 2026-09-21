from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # b -> a
        in_degrees = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            in_degrees[a] += 1
        
        stack = []
        for i, degree in enumerate(in_degrees):
            if degree == 0:
                stack.append(i)
        
        res = []
        while stack:
            course = stack.pop()
            res.append(course)
            for neighbor in adj[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    stack.append(neighbor)
            
        if len(res) != numCourses:
            return []
        else:
            return res