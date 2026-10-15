class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1, 2, 3, 2, 2
        # 1 -> 2 <-> 3 



        # we need to find the start of the cycle in O(1) space
        # Use fast and slow pointer to find a cycle
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        # Find the start by using two slow pointers (one from head) other from the connection point until they meet
        p1, p2 = 0, slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        
        return p2