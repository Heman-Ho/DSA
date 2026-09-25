from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        adj = defaultdict(list)
        courses_taken = 0

        # create a graph of b -> a for all b is prereq of a
        for a, b in prerequisites:
            adj[b].append(a)
            in_degrees[a] += 1

        q = deque()
        for i, num in enumerate(in_degrees):
            if num == 0:
                q.append(i)
                courses_taken += 1
        
        # Topological sort
        while q:
            qLen = len(q)
            for i in range(qLen):
                course = q.popleft()
                for neighbor in adj[course]:
                    in_degrees[neighbor] -= 1
                    if in_degrees[neighbor] == 0:
                        q.append(neighbor)
                        courses_taken += 1

        return courses_taken == numCourses

        
                