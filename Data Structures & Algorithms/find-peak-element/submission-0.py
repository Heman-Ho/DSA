class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            cur_num = nums[m]
            left_num = float('-inf') if m == 0 else nums[m-1]
            right_num = float('-inf') if m == (len(nums) - 1) else nums[m+1]
            
            if left_num < cur_num > right_num:
                return m
            
            if left_num < cur_num < right_num:
                # we are on an increasing segment so a peak must lie on the right of m
                l = m + 1
            else: # we are on a decreasing segment, or a valley both cases imply there is a peak to the left of m 
                r = m - 1

        