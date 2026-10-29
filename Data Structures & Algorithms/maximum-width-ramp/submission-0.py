class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, v in enumerate(nums):
            if not stack or nums[stack[-1]] > v:
                stack.append(i)

        # 4 1 2 3 5 
        # stack = 0 1

        max_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)
            if not stack:
                break

        return max_width