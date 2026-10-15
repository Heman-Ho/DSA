class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_products = [1] * n
        post_products = [1] * n

        for i in range(1, n):
            pre_products[i] = nums[i-1] * pre_products[i-1]
        
        
        for i in range(n - 2, -1, -1):
            post_products[i] = post_products[i+1] * nums[i+1]
        
        res = [1] * n
        for i in range(n):
            res[i] = pre_products[i] * post_products[i]
        return res