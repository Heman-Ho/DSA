class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directory = []

        # Parse path from left to right, adding directories into a stack
        for i in range(1, len(path)):
            c = path[i]
            if c == '/':
                new_dir = "".join(directory)

                # if directory == "../" => pop one from the stack
                if new_dir == "..":
                    if stack:
                        stack.pop()
                elif len(new_dir) != 0 and new_dir != ".":
                    stack.append(new_dir)
                directory = []

            else:
                directory.append(c)
        
        new_dir = "".join(directory)
        if new_dir == "..":
            if stack:
                stack.pop()
        elif len(new_dir) != 0 and new_dir != ".":
            stack.append(new_dir)
        
        return "/" + "/".join(stack)