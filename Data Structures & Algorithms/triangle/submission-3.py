class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # for each level in triangle
        prev = triangle[0]
        for r in range(1, len(triangle)):
            cur = [0] * len(triangle[r])
            for i in range(len(cur)):
                top_left = prev[i - 1] if i - 1 >= 0 else float('inf')
                top_right = prev[i] if i < len(prev) else float('inf')
                cur[i] = triangle[r][i] + min(top_left, top_right)
            
            prev = cur
        
        return min(prev)
       
