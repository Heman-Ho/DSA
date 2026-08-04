class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #      2,            -2
        #   0,   4,      -4,    0
        # -2, 2, 2, 6, -6, -2, -2, 2

        res = 0

        def backtrack(i, cur_sum):
            nonlocal res
            if i >= len(nums):
                if cur_sum == target:
                    res += 1
                return
           
            backtrack(i + 1, cur_sum + nums[i])
            backtrack(i + 1, cur_sum - nums[i])
        
        backtrack(0, 0)

        return res