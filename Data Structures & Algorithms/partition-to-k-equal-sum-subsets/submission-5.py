class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Use a brute force approach with backtracking
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k

        used = [False] * len(nums)
        
        def dfs(i, cur_sum, k_remaining):
            if k_remaining == 0:
                return True
            if cur_sum == target:
                return dfs(0, 0, k_remaining - 1)

            for j in range(i, len(nums)):
                # Prune early
                if used[j] or cur_sum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j+1, cur_sum + nums[j], k_remaining):
                    return True
                used[j] = False

            return False
        return dfs(0, 0, k)
            