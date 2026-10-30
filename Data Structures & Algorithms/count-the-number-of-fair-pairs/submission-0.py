class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # approach 1: n^2 brute force check with 2 pointers
        # approach 2: sort nums, for each number, use binary search to find the range

        nums.sort()
        res = 0

        def find_lower(l, r, target):
            # returns the lowest index of numbers >= target
            if nums[r] < target: 
                return r + 1

            while l < r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            
            return l


        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            low_target = lower - num
            high_target = upper - num + 1

            # bin search to find the smallest index such that num + nums[m] > lower
            l_bound = find_lower(l, r, low_target)

            # bin search to find the largest index such that num + nums[m] < upper
            r_bound = find_lower(l, r, high_target)
            
            if r_bound > l_bound:
                res += r_bound - l_bound
        
        return res
        '''
        upper = 3, lower = -1
        [-3, 1, 2, 5]
        num = -3

        l = 1, r = 3
        low_target = 2
        high_target = 7
        '''