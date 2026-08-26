class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        state = 0 # 0: neither, 1: increasing, 2: decreasing
        cur = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                state = 0
                cur = 1
            elif nums[i-1] < nums[i]:
                if state == 1:
                    cur += 1
                else:
                    state = 1
                    cur = 2
            else:
                if state == 2:
                    cur += 1
                else:
                    state = 2
                    cur = 2
            best = max(best, cur)
        return best