class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ord_in = sum(ord(c) for c in s)
        ord_out = sum(ord(c) for c in t)

        return chr(ord_out - ord_in)