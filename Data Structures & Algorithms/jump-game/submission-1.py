class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        l, r = 0, nums[0]

        while l <= r:
            r = max(r, l + nums[l])
            if r >= len(nums) - 1:
                return True
            l += 1

        return False
        # 1, 2, 0, 1, 0
        #          L 
        #          R 