class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        num_jumps = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            num_jumps += 1

        return num_jumps