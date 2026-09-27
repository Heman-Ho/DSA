class Solution:
    def trap(self, height: List[int]) -> int:
        # Keep track of left max and right max
        # Use 2 pointers, shifting the side with the lower max 
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:   
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(0, min(leftMax, rightMax) - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(0, min(leftMax, rightMax) - height[r])
        
        return res

            

