# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        countA = countB = 0

        while curA:
            countA += 1
            curA = curA.next
        
        while curB:
            countB += 1
            curB = curB.next
        
        if countA < countB:
            countA, countB = countB, countA
            headA, headB = headB, headA
        
        # we know countA > countB and headA holds the longer list
        curA, curB = headA, headB

        for _ in range(countA - countB):
            curA = curA.next
        
        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA