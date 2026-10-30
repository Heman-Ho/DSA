from collections import deque
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # min heap of size k
        min_heap = [] 
        q = deque()

        q.append(root)
        
        while q:
            q_len = len(q)
            cur_sum = 0
            for _ in range(q_len):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(min_heap, cur_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        if len(min_heap) < k:
            return -1 
            
        return min_heap[0]