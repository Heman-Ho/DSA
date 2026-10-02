class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for c in bin(n):
            if c == "1":
                res += 1
        return res
