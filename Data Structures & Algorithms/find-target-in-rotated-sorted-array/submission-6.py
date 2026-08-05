class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l  + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                # 4,5,6,7,8,0,1,2,3
                #   l   m     r
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 4,5,6,7,0,1,2,3
                #     l,    m,  r
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

                    