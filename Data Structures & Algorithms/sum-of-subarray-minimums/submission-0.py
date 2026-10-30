class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # prev_less[i]: index of nearest element to the LEFT with value < arr[i], or -1
        prev_less = [-1] * n
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        # next_less_eq[i]: index of nearest element to the RIGHT with value <= arr[i], or n
        next_less_eq = [n] * n
        stack = []
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                next_less_eq[stack.pop()] = i
            stack.append(i)

        total = 0
        for i, v in enumerate(arr):
            left = i - prev_less[i]
            right = next_less_eq[i] - i
            total = (total + v * left * right) % MOD

        return total