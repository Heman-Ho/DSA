class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [] 
        n = len(pushed)

        push_i = 0
        pop_i = 0

        for push_i in range(n):
            stack.append(pushed[push_i])

            while stack and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1
            
        return len(stack) == 0

        # 4, 2, 3, 1
        # 2, 1, 4, 3
        # [4, 3]