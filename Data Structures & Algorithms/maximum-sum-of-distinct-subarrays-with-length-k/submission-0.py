class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        
        l = 0
        counts = set()
        cur_sum = 0
        res = 0

        for r in range(len(nums)):
            while nums[r] in counts or (r - l + 1) > k:
                counts.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            counts.add(nums[r])
            cur_sum += nums[r]
            
            if r - l + 1 == k:
                res = max(res, cur_sum)
        
        return res