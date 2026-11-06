class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        m = len(nums) // 2

        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m+1:])

        new_node = TreeNode(nums[m])
        new_node.left = left
        new_node.right = right
        
        return new_node
