class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        used = nums[0]
        cur_idx = 1
        for i in range(1, len(nums)):
            if nums[i] == used:
                continue
            nums[cur_idx] = nums[i]
            used = nums[i]
            cur_idx += 1
        return cur_idx