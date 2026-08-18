class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # prefix_gas  = [1, 3, 6, 10, 15]
        # prefix_cost = [3, 7, 12, 13, 15]
        # [-2, -2, -2, +3, +3]
        # [-2, -4, -6, -3, 0] => choose the station after the absolute min

        # if prefix_cost[-1] > prefix_gas[-1]: return -1

        delta = [gas[i] - cost[i] for i in range(n)]
        prefix_delta = [0] * n
        prefix_delta[0] = delta[0]
        for i in range(1, n):
            prefix_delta[i] = delta[i] + prefix_delta[i-1]
        
        if prefix_delta[-1] < 0:
            return -1
        
        minimum = float('inf')
        min_idx = 0
        for i, num in enumerate(prefix_delta):
            if num < minimum:
                minimum = num
                min_idx = i
        return (min_idx + 1) % n


        # [2, -1, -1]
        # [2, 1, 0]
