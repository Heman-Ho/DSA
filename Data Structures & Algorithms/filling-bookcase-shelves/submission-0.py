class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        # dp[i] stores the minimum total height for the first i books
        dp = [float("inf")] * (n + 1)
        dp[0] = 0  # 0 books require 0 height

        for i in range(1, n + 1):
            curr_width = 0
            curr_height = 0

            # Try forming a shelf backwards from book i down to book 1
            # looping forwards would reuse 
            for j in range(i, 0, -1):
                thickness, height = books[j - 1]

                curr_width += thickness
                if curr_width > shelfWidth:
                    break  # Cannot fit more books on this shelf

                curr_height = max(curr_height, height)

                # dp[j - 1] is the best arrangement before this shelf started
                dp[i] = min(dp[i], dp[j - 1] + curr_height)

        return dp[n]