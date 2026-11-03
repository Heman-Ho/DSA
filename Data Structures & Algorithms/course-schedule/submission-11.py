class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for a, b in prerequisites:
            # b -> a
            in_degrees[a] += 1
            adj[b].append(a)

        q = deque()
        
        for i in range(numCourses):
            if in_degrees[i] == 0:
                q.append(i)
        
        courses_taken = 0
        while q:
            course = q.popleft()
            courses_taken += 1
            
            for neighbor in adj[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)
            
        return courses_taken == numCourses


