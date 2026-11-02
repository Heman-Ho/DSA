class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # max contiguous subarray size of fruits with 2 items 
        res = 0
        l = 0

        counts = {}

        for r in range(len(fruits)):
            counts[fruits[r]] = counts.get(fruits[r], 0) + 1

            while len(counts) > 2:
              
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res