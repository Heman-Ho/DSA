# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        # 5 -> 6 -> 7 -> 1 -> 2 -> 3 -> 4
        if not head:
            return None

        # mod k by len of the LL
        n = 0
        cur = head
        tail = cur

        while cur:
            tail = cur
            cur = cur.next
            n += 1
        
        k %= n

        tail.next = head

        # locate new tail
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next
        
        # get new head
        new_head = cur.next

        # set  new tail next = None
        cur.next = None

        return new_head


