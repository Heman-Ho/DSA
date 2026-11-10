class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        # Step 1: Reverse the linked list
        head = reverse(head)
        
        # Step 2: Track maximum value and filter out smaller nodes
        curr = head
        max_val = head.val
        
        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next  # Remove node
            else:
                max_val = curr.next.val
                curr = curr.next
                
        # Step 3: Reverse back to restore original order
        return reverse(head)