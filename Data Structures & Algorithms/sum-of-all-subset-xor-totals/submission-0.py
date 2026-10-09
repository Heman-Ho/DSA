class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        cur = 0

        def backtrack(i):
            nonlocal res
            nonlocal cur
            res += cur

            for j in range(i, len(nums)):
                cur ^= nums[j] 
                backtrack(j+1)
                cur ^= nums[j]       
        
        backtrack(0)
        return res

        # res = 2 + 6 
        # cur = 6