class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()
        
        for i in range(k):
            if i >= len(nums):
                return False

            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
        
        l = 0
        for r in range(k, len(nums)):
            if nums[r] in nums_set:
                return True
            nums_set.add(nums[r])
            nums_set.remove(nums[l])
            l += 1
        
        return False