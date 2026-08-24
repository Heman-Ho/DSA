class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # we can model this problem as exploring a decision tree using backtracking. 
        # at each decision level, we choose whether we want to include the current number or not. 
        # When our current path reaches k numbers, we add that to our result array as a valid combination
        res = [] 
        path = [] 

        def backtrack(i): 
            if len(path) == k:
                res.append(path.copy())
            
            for j in range(i, n + 1):
                path.append(j)
                backtrack(j+1)
                path.pop()

        backtrack(1)
        return res
