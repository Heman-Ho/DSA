class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #      2,            -2
        #   0,   4,      -4,    0
        # -2, 2, 2, 6, -6, -2, -2, 2

        
        memo = {}
        def backtrack(i, cur_sum):
            if i >= len(nums):
                if cur_sum == target:
                   return 1
                else:
                    return 0

            state = (i, cur_sum)
            if state in memo:
                return memo[state]

            add_way = backtrack(i + 1, cur_sum + nums[i])
            sub_way = backtrack(i + 1, cur_sum - nums[i])
            memo[state] = add_way + sub_way
            return add_way + sub_way
        
        return backtrack(0, 0)
