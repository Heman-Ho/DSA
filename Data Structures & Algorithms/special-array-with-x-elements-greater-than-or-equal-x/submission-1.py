class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, 1

        while i < n and j <= n:
            while i < n and j > nums[i]:
                i += 1

            if j == n - i:
                return j
            j += 1

        return -1