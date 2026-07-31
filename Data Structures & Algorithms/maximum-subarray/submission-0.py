class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        best_sum = float('-inf')

        for num in nums:
            if num + cur_sum < num: 
                cur_sum = num
            else:
                cur_sum += num
            best_sum = max(best_sum, cur_sum)
        return best_sum