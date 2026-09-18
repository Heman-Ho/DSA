class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for j in range(len(nums)):
                if j in used: 
                    continue
                perm.append(nums[j])
                used.add(j)
                backtrack()
                perm.pop()
                used.remove(j)
        backtrack()
        return res

