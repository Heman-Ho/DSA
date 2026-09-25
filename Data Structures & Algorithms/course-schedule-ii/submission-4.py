from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ordering = []
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b, in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1
        
        q = deque()
        for i, num in enumerate(in_degree):
            if num == 0:
                q.append(i)

        while q:
            course = q.popleft()
            ordering.append(course)

            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
            
        return ordering if len(ordering) == numCourses else []