class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Run a dfs on each node to see if it there is a cycle
        # Use a hashmap mappig course:[list of prereqs] for the dfs
        # After visiting a prereq, we can remove it from the list to avoid double traversal
        # Use a visited set to check for cycle
        visited = set()
        course_prereqs = {}

        # Build the hash map (course:[list of prereqs])
        for course in range(numCourses):
            course_prereqs[course] = []
        for course, prereq in prerequisites:
                course_prereqs[course].append(prereq)
        
        def dfs(course):
            # There is a cycle in the graph
            if course in visited:
                return False
            # The current course has no more prerequisites (or we already calculated that it's prereqs can be fulfilled)
            if course_prereqs[course] == []:
                return True

            visited.add(course)

            # Check each of it's prerequisites if they can be fulfilled
            for prereq in course_prereqs[course]:
                if not dfs(prereq):
                    return False

            # If all prereqs can be fulfilled, we can makrk the current node as [] to avoid additional work 
            course_prereqs[course] = []

            # Remove course from visited because 
            visited.remove(course)

            return True

        for course, _ in prerequisites:
            if dfs(course) == False:
                return False
        return True