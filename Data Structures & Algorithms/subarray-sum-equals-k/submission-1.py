from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        complements = defaultdict(int)
        complements[0] = 1

        res = 0
        cur_sum = 0

        # for every prefix as we traverse nums, 
        for num in nums:
            cur_sum += num

            # cur_sum - prev_sum = k => we need prev_sum = cur_sum - k
            complement = cur_sum - k

            # if it's complement is in complements, add to res
            res += complements[complement]
            
            # add cur prefix sum to complements
            complements[cur_sum] += 1

        return res
        