class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        l = 0
        cur_sum = 0
    
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target and l <= r:
                best = min(best, r - l + 1)
                cur_sum -= nums[l]
                l += 1
                
            
        if best == float('inf'):
            return 0
        return best
            
