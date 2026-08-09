from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            count[s[r]] += 1
            # Track the highest frequency of ANY single character seen in the current window
            max_freq = max(max_freq, count[s[r]])

            # If the number of characters to replace exceeds k, shrink window from left
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


