"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # traverse the orig LL and create a copy of it without random pointer
        # A -> B -> C -> None
        # dummy_new -> None
        
        dummy_new = Node(0, None, None)
        p1, p2 = head, dummy_new
        old_to_new = {}
        old_to_new[None] = None

        while p1:
            # while traversing, map old_node to new_node
            p2.next = Node(p1.val, None, None)
            old_to_new[p1] = p2.next
            p1 = p1.next
            p2 = p2.next
        
        # traverse through the orig LL and the new LL to update the random node using the map
        p1, p2 = head, dummy_new.next
        while p1:
            p2.random = old_to_new[p1.random]
            p1 = p1.next
            p2 = p2.next
        
        return dummy_new.next
