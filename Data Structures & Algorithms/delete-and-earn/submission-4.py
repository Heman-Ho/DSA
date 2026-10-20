class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        points = defaultdict(int)

        for num, count in counts.items():
            points[num] = num * count
        
        n = max(nums)
        dp = [0] * (n + 1) # dp[i] represents the max score of using nums up to val i
        dp[1] = points[1]

        for i in range(2, n + 1): 
            dp[i] = max(dp[i-2] + points[i], dp[i-1])
        return dp[-1]