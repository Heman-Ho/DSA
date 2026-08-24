class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        seen = [False] * len(nums)

        def backtrack(i: int) -> None:
            # Every branch of the recursion is a valid subset => we only recurse on valid subsets (and non duplicates)
            res.append(path.copy())
      
            for j in range(i, len(nums)):
                # either use the cur number or don't use it
                # skip duplicate choice if we are at the same decision level
                if j > 0 and nums[j] == nums[j-1] and not seen[j-1]:
                    continue

                # We choose to use the current num at index i
                seen[j] = True
                path.append(nums[j])

                # explore the path 
                backtrack(j+1)

                # undo the choice
                seen[j] = False
                path.pop()

        backtrack(0)
            
        return res

                
