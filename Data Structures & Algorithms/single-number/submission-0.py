class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use the xor operator on all numbers. Since every integer appears twice, they cancel each other
        res = 0
        for num in nums:
            res ^= num
        return res