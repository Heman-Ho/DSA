from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # course a has an edge to course b if a is a prereq of b
        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            in_degrees[a] += 1

        # do a topological sort on all the courses
        q = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)

        # process all nodes with indegree of 0
        courses_taken = 0

        while q:
            node = q.popleft()
            courses_taken += 1

            # for all neighbors of the node, decrement its indegree
            for neighbor in adj[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)
        
        return courses_taken == numCourses