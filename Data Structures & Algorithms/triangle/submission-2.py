class Solution:

  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # Start with a copy of the bottom row
    dp = triangle[-1].copy()

    # Move upwards from the second-to-last row to the top
    for r in range(len(triangle) - 2, -1, -1):
      for c in range(r + 1):
        dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

    return dp[0]