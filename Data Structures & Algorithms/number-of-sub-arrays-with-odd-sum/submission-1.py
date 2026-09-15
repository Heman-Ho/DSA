class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = [1, 0]
        prefix = res = 0
        MOD = 10**9 + 7

        for num in arr:
            prefix = (prefix + num) % 2
            res = (res + count[1 - prefix]) % MOD
            count[prefix] += 1

        return res