# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Build two stacks out of l1 and l2 
        stack1 = [] 
        stack2 = [] 

        cur = l1
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2

        while cur:
            stack2.append(cur.val)
            cur = cur.next
        
        # 2. Using the 2 stacks, create the sum of them in another stack
        res_stack = [] 
        carry_on = 0

        while stack1 or stack2 or carry_on:
            num1 = 0 if not stack1 else stack1.pop()
            num2 = 0 if not stack2 else stack2.pop()

            new_num = num1 + num2 + carry_on
            carry_on = new_num // 10
            new_num %= 10
            res_stack.append(new_num)
        
        # 3. Use the stack to form resulting linked list 
        dummy = ListNode()
        cur = dummy

        while res_stack:
            new_node = ListNode(res_stack.pop())
            cur.next = new_node
            cur = cur.next
        
        return dummy.next

         
