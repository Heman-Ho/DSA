class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0 
        cur = 0
        for num in nums:
            if num != 1:
                res = max(res, cur)
                cur = 0
            else:
                cur += 1
                res = max(res, cur)
        
        return res