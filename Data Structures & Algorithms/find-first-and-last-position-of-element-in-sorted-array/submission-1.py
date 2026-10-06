import math
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        # if middle < target => l = m + 1
        # else r = m

        #  ... 1 3 3 3 3 4 ,...
        #  l             m      

        l, r = 0, len(nums) - 1

        res = [0, 0]
        

        # binary search and converge on left target in log n
        while l < r:
            m = (l + r) // 2
            print(f"pass 1: middle: {m}, left: {l}, right: {r}")

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        res[0] = l

        # second pass binary search to converge on right target in O(log n)

        # 5 7 7 8 8 10
        #         l
        #         m r
        # l: 4
        # r: 5
        # m: 4

        
    
             

        l, r = 0, len(nums) - 1
        while l < r:
            m = math.ceil((l + r) / 2)
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        res[1] = l

        # return result
        if l < 0 or l >= len(nums) or nums[l] != target:
            return [-1, -1]
        else:
            return res