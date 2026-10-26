class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        seen = defaultdict(int)

        def backtrack(i):
            nonlocal res
            
            for j in range(i, len(nums)):
                above = nums[j] + k
                below = nums[j] - k

                if seen[above] != 0 or seen[below] != 0:
                    continue

                res += 1

                seen[nums[j]] += 1
                backtrack(j + 1)
                seen[nums[j]] -= 1
            
        backtrack(0)

        return res

        """
        [1, 3, 5]
        res: 1
        seen = {
            1: 1
        }
        """