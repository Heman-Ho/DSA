from bisect import bisect_left

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            lo = bisect_left(nums, lower - num, i + 1)
            hi = bisect_left(nums, upper - num + 1, i + 1)
            res += hi - lo
        return res