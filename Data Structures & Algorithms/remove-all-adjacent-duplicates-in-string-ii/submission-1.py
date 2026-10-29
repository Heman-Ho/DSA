class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []   # [(char, consecutive_count), ...]

        for c in s:
            if stack and stack[-1][0] == c:
                char, count = stack[-1]
                if count + 1 == k:
                    stack.pop()
                else:
                    stack[-1] = (char, count + 1)
            else:
                stack.append((c, 1))

        return "".join(char * count for char, count in stack)