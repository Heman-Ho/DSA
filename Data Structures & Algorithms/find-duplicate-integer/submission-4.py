class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p = 0
        while nums[p] != -1:
            nxt = nums[p]
            nums[p] = -1
            p = nxt
        return p