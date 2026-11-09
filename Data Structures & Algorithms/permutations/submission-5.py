class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                path.append(num)
                backtrack()
                path.pop()
                seen.remove(num)
            
        backtrack()
        return res