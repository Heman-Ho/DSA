# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2 = head.next, dummy

        new_val = 0

        while p1:
            if p1.val == 0:
                new_node = ListNode(new_val)
                p2.next = new_node
                p2 = p2.next
                new_val = 0
            new_val += p1.val
            p1 = p1.next
        
        return dummy.next
