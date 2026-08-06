class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Let dp[i,j] represent the min distance from the first i letters of word1 and the first j letters of word2
    
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Base Case: 
        # If we are using 0 letters from word1 or 0 letters from word2, then we must only use add operations
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            dp[i][0] = i

        # Build up the dp table
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # Case: no need to change because letters equal
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1]
                # Case: we add a letter
                # Case: we delete a letter
                # Case: we replace a letter
           
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)

        return dp[-1][-1]
            

                