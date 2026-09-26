class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # let dp[i] hold whether s[:i+1] (first i letters) can be segmented by the words in wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word):
                    if dp[i-len(word)] and word == s[i-len(word):i]:
                        dp[i] = True
                        break

        return dp[len(s)]