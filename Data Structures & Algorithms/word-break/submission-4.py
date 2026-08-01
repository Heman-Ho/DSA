from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        @cache
        def helper(i):
            if i >= len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet and helper(j+1):
                        return True
            return False
        return helper(0)