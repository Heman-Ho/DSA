class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = [] 
        nums.sort()

        def backtrack(i): 
            if sum(path) == target:
                res.append(path.copy())
                return 
       
            for j in range(i, len(nums)):
                if sum(path) + nums[j] > target:
                    return
                path.append(nums[j])
                backtrack(j)
                path.pop()

        backtrack(0)
        return res
