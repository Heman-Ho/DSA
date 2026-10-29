class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while stack and k > 0 and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        # If digits were non-decreasing we never used all of k — trim from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Strip leading zeros
        result = "".join(stack).lstrip("0")
        return result if result else "0"