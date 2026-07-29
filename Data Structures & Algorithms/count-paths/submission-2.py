class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # let dp[i,j] represent the number of ways you can reach dp[i,j]
        # dp[i,j] = dp[i-1,j] + dp[i, j-1]
        # We can fill in this matrix row by row and return dp[m-1, n-1]
        # Since we fill in the matrix row by row, we can keep track of the prev
        # row and use O(n) space instead of O(mn) space
        prev_row = [1 for _ in range(n)]
        cur_row = [1 for _ in range(n)]
        for r in range(1, m):
            cur_row[0] = prev_row[0]
            for c in range(1, n):
                cur_row[c] = cur_row[c-1] + prev_row[c]
            prev_row = cur_row

        return cur_row[n-1]