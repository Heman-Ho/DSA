class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        # sort nums
        nums.sort()
        # -2, 0, 0, 2, 2

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            target = -num
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                  
                elif nums[l] + nums[r] > target:
                    r -= 1
                else: l += 1
            
        return res