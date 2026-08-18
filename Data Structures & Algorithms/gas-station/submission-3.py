class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        running_prefix = 0
        min_prefix = float('inf')
        min_idx = 0
        n = len(gas)

        for i in range(n):
            running_prefix += gas[i] - cost[i]
            if running_prefix < min_prefix:
                min_prefix = running_prefix
                min_idx = i

        # If total gas < total cost, completion is impossible
        if running_prefix < 0:
            return -1

        # The start idx must be the one after the lowest point 
        return (min_idx + 1) % n