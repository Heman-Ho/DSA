from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()

        # Create an adjacency list which maps course -> set of prereqs
        adj = {}
        for course in range(numCourses):
            adj[course] = set()
        for course, prereq in prerequisites:
            adj[course].add(prereq)

        print(adj)
        # At each step, take all the courses in an arbitrary order that have no prerequisites
        while True:
            if len(res) == numCourses:
                return res

            progress = False
            for course in adj:
                if not adj[course] and course not in visited:
                    progress = True
                    res.append(course)
                    # Mark that course as visited
                    visited.add(course)
                    # remove that course from the prerequisite set of other courses 
                    for other_course in adj:
                        adj[other_course].discard(course)
            if not progress:
                return []
       
            