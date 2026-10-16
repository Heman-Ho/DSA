class MinStack:

    def __init__(self):
        self.stack = [] # will hold tuple (top_val, min_val)
       
    def push(self, val: int) -> None:
        # case 1: stack is empty
        if not self.stack:
            self.stack.append((val, val))
        
        # case 2: stack is not empty
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
