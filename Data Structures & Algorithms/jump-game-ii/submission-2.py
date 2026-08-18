class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        cur_end = 0
        farthest = 0

        # Stop at len(nums) - 1 because the destination is already reached
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == cur_end:
                num_jumps += 1
                cur_end = farthest

        return num_jumps