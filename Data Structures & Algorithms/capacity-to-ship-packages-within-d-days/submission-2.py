class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The answer lies in the range(max(weights), sum(weights)) assuming we can't ship a portion of a package
        # Use a binary search to test the answers in the answer space
        # To test an answer we need to simulate it by going through the weights
        #  Time comlexity = O(NlogM) where N is num weights and m is sum(weights)
        r = sum(weights)
        l = max(weights)

        def can_ship(capacity):
            cur_days = 1
            cur_capacity = capacity
            for weight in weights:
                if cur_capacity < weight:
                    cur_days += 1
                    if cur_days > days:
                        return False
                    cur_capacity = capacity
                cur_capacity -= weight
            return True

        best = l
        while l <= r:
            m = (l + r) // 2            
            if can_ship(m):
                best = m
                r = m - 1
            else:
                l = m + 1
        return best