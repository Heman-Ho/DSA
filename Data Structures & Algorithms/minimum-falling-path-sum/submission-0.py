class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        
        for r in range(1, n):
            for c in range(n):
                left = matrix[r - 1][c - 1] if c > 0 else float('inf')
                mid = matrix[r - 1][c]
                right = matrix[r - 1][c + 1] if c < n - 1 else float('inf')
                
                matrix[r][c] += min(left, mid, right)
                
        return min(matrix[-1])