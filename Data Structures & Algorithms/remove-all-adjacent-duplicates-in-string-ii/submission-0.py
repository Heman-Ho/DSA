class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        c_stack = []
        num_stack = []
        for c in s:
            if c_stack and c_stack[-1] == c and num_stack[-1] == k - 1:
                for _ in range(k-1):
                    c_stack.pop()
                    num_stack.pop()
            else:
                num_consecutive = 1 if not c_stack or c_stack[-1] != c else num_stack[-1] + 1
                c_stack.append(c)
                num_stack.append(num_consecutive)
        
        return "".join(c_stack)