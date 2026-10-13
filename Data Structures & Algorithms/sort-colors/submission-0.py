class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = Counter(nums)
        
        i = 0
        for val in range(3):
            cnt = counts[val]
            for _ in range(cnt):
                nums[i] = val
                i += 1
        
