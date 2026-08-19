from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        counts = Counter(nums)
        res = []
        for num, count in counts.items():
            if count > n:
                res.append(num)
        return res