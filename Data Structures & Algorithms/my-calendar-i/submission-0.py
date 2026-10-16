class TreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def _insert(self, node: TreeNode, start: int, end: int) -> bool:
        if end <= node.start:
            if not node.left:
                node.left = TreeNode(start, end)
                return True
            return self._insert(node.left, start, end)
        elif start >= node.end:
            if not node.right:
                node.right = TreeNode(start, end)
                return True
            return self._insert(node.right, start, end)
        else:
            return False

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime, endTime)
            return True
        return self._insert(self.root, startTime, endTime)