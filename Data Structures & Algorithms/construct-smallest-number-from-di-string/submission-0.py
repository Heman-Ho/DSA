class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        answer = []
        for i in range(len(pattern)+1):
            stack.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I':
                while stack: 
                    answer.append(stack.pop())
        return ''.join(answer)


        #IDDDDD
        # 165432
        # stack = [2, 3, 4, 5, 6]