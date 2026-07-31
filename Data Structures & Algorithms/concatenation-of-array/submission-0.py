class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for multiplier in range(2):
            for i in range(n):
                ans[multiplier*(n) + i] = nums[i]
        
        return ans