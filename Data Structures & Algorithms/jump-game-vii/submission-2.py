class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == "1":
            return False

        dp = [False] * n
        dp[0] = True
        reachable_count = 0

        for i in range(1, n):
            # Add new valid origin entering the window
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
            # Remove old origin falling outside the window
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1

            if s[i] == "0" and reachable_count > 0:
                dp[i] = True

        return dp[-1]