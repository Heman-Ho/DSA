from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create an array of prefix sums prefixes[i] = sum(nums:i)
        # [2,-1,1,2]
        # [0,2,1,2,4], k = 2, res = 4


        # 0: 1
        # prefix_sum = 2


        # add each to a map and include its count
        prefix_sum = 0
        res = 0
        counts = defaultdict(int)
        counts[0] += 1
        
        for num in nums:
            prefix_sum += num
            target = prefix_sum - k

            if target in counts:
                res += counts[target]

            counts[prefix_sum] += 1

        return res