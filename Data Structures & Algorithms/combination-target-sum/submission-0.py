class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = [] 

        def backtrack(i): 
            if sum(path) == target:
                res.append(path.copy())
                return
            if sum(path) > target:
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j)
                path.pop()

        backtrack(0)
        return res
