class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        stack = []
        best = 0
        for right in range(n + 1):
            current = nums[right] if right < n else 0
            while stack and nums[stack[-1]] >= current:
                index = stack.pop()
                left = stack[-1] + 1 if stack else 0
                best = max(best, nums[index] * (prefix[right] - prefix[left]))
            if right < n: stack.append(right)
        return best % 1000000007
