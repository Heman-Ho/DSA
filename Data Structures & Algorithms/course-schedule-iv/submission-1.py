class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create a reachibility matrix
        # let A[i,j] represent whether i can reach j (meaning i is a direct or transitive prereq of j)
        A = [[False] * numCourses for _ in range(numCourses)]

        # Fill in base cases
        for prereq, course in prerequisites:
            A[prereq][course] = True
        
        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    if A[i][j]:
                        break
                    A[i][j] = A[i][k] and A[k][j]
        
        return [A[i][j] for i, j in queries]