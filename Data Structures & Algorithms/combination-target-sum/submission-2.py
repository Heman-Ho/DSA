class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = [] 
        nums.sort()

        def backtrack(i, val): 
            if val == target:
                res.append(path.copy())
                return 
       
            for j in range(i, len(nums)):
                if val + nums[j] > target:
                    return

                path.append(nums[j])
                backtrack(j, val + nums[j])
                path.pop()

        backtrack(0, 0)
        return res
