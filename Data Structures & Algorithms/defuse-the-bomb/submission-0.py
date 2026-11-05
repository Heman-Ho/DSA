class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        # Duplicate the array so any wrap-around window is contiguous
        doubled = code + code
        prefix = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix[i + 1] = prefix[i] + doubled[i]

        def window_sum(l, r):
            return prefix[r + 1] - prefix[l]

        res = [0] * n
        for i in range(n):
            if k > 0:
                # next k elements after i: indices i+1 .. i+k
                l, r = i + 1, i + k
            else:
                l, r = i + k + n, i - 1 + n
            res[i] = window_sum(l, r)

        return res