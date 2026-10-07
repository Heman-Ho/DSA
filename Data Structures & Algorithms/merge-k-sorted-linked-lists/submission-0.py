import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            cur.next = node                    # reuse node, don't allocate
            cur = cur.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next