class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        
        l = 0
        cur_sum = sum(arr[:k])
        res = 1 if cur_sum // k >= threshold else 0

        for r in range(k, len(arr)):
            cur_sum += arr[r]
            cur_sum -= arr[l]
            l += 1

            if cur_sum // k >= threshold:
                res += 1
        
        return res
            

            