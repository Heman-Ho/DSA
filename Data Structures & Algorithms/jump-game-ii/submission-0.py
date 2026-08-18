class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        cur_idx = 0
        furthest_reach = 0

        while furthest_reach < len(nums) - 1:
            
            for i in range(cur_idx, furthest_reach + 1):
                furthest_reach = max(furthest_reach, nums[i] + i)
            num_jumps += 1
            cur_idx = i
        
        return num_jumps