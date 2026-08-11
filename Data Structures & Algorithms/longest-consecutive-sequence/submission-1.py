class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        best_seq = 0
        while nums_set:
            # Choose an arbitrary value in the set
            cur_seq = 0
            num = nums_set.pop()

            # expand to the left and to the right of the value to calculate the length of it's sequence
            right = num + 1
            left = num - 1
            while right in nums_set:
                nums_set.remove(right)
                right += 1
            while left in nums_set:
                nums_set.remove(left)
                left -= 1

            best_seq = max(best_seq, right - left - 1)
        return best_seq