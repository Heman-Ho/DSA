class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = float('-inf')

        for num in nums:
            # greedily choose to start a new subarray or continue the previous subarray
            cur_sum = max(cur_sum + num, num)
            # Keep track of the best subarray found
            best_sum = max(best_sum, cur_sum)
        return best_sum