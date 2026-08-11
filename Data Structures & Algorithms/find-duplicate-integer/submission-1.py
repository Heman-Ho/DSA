class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Notice that nums can be represented as a linked list where the start of the cycle 
        # is the repeated number.
        # each index i represents a node, and nums[i] represents node.next
        # Since nums is in range[1,n], we know that no node points to index 0, 
        # so we can use index 0 as the head.
        # 1. detect cycle and find meeting point of fast and slow pointers
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        # 2. Set one of the pointers to head
        slow = 0

        # 3. move each pointer at the same speed until they meet at the cycle start
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow