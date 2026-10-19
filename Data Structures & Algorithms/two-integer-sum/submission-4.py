class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {} # maps complement -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
        
        