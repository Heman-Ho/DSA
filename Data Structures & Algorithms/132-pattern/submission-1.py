class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []           # candidate "3" values, monotonically decreasing 
        max_k = float('-inf')  # best "2" seen so far

        for x in reversed(nums):
            if x < max_k:
                return True
            while stack and stack[-1] < x:
                max_k = stack.pop()   # this popped value had something bigger (x) to its right
            stack.append(x)

        return False