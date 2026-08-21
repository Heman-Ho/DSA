class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #       ___
        # ...__/     ____ ...
        #           /  
        #          /
        #    l   m    r

        # case nums[l] < nums[m]: if target >= nums[l] and <= nums[m] then the target is between l and m
        # case nums[m] < nums[r]: and target is >= nums[m] and <= nums[r] we k now the target is between m and r
        # Case nums[m] = nums[l] = nums[r] we shift the l and r boundaries inward
        l, r = 0, len(nums) - 1
        while l <= r:
            print(f"searching between {l} and {r}")
            m = (l + r) // 2

            if nums[m] == target:
                return True

            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else: l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False
            
