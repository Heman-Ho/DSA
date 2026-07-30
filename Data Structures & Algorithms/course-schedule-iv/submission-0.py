class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # map course: list of prereqs
        adj = {course: [] for course in range(numCourses)}
        for prereq, course in prerequisites:
            adj[course].append(prereq)
        
        # uj is a prereq of vj iff uj -> ... -> vj

        # Create a set of traveresed courses so that we don't dfs through loops
        seen = set()

        def dfs(course, target):
            if adj[course] == [] or course in seen:
                seen.add(course)
                return False
            if target in adj[course]:
                return True
            seen.add(course)
            for prereq in adj[course]:
                if dfs(prereq, target):
                    return True
            return False

        res = []
        for prereq, course in queries: 
            seen = set()
            res.append(dfs(course, prereq))
        return res