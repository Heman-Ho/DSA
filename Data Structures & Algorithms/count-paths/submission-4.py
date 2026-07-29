class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # let dp[i,j] represent the number of ways you can reach dp[i,j]
        # dp[i,j] = dp[i-1,j] + dp[i, j-1]
        # We can fill in this matrix row by row and return dp[m-1, n-1]
        # Since we fill in the matrix row by row, we can keep track of the prev
        # row and use O(n) space instead of O(mn) space

        cur_row = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                cur_row[c] = cur_row[c-1] + cur_row[c]

        return cur_row[n-1]