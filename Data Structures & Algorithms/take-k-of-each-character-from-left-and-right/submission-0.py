from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if any(total[c] < k for c in 'abc'):
            return -1

        limit = {c: total[c] - k for c in 'abc'}
        window = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            # shrink until window is feasible
            while window[ch] > limit[ch]:
                window[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return len(s) - best