class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * (len(nums))# left_products[i] represents the product of nums[:i]
        right_products = [1] * (len(nums))

        for i in range(1, len(left_products)):
            left_products[i] = left_products[i-1] * nums[i-1]
        for i in range(len(right_products)-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
        
        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = left_products[i] * right_products[i]
        
        return res