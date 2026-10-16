class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3

        for num in nums:
            counts[num] += 1
        
        insert_pos = 0

        for color, count in enumerate(counts):
            for _ in range(count):
                nums[insert_pos] = color
                insert_pos += 1
        
