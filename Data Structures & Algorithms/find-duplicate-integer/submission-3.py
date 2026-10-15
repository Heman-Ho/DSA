class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # -1, -1, -1, 2, 2
      
        p = 0
        nextp = 0
        while True:
            if nums[nextp] == -1:
                return prev

            nextp = nums[p]
            prev = nums[p]
            nums[p] = -1
            p = nextp
        
        