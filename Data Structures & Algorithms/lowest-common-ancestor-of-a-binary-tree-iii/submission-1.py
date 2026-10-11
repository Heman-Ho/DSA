"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.parent
            return h

        h1, h2 = height(p), height(q)
        if h2 < h1:
            p, q = q, p

        diff = abs(h1 - h2)
        while diff:
            q = q.parent
            diff -= 1

        while p != q:
            p = p.parent
            q = q.parent

        return p