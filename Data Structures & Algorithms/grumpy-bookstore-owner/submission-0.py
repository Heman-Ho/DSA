class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Sum up customers that are guaranteed to be satisfied (owner not grumpy)
        n = len(customers)
        num_satisfied = 0 
        for i in range(n):
            if not grumpy[i]:
                num_satisfied += customers[i]

        # Use a sliding window on the grumpy arr & customers arr to maximize
        # the number number of customers we can convert from unsatisfied -> sat
        max_converted = 0
        cur_converted = 0
        l = 0

        for r in range(n):
            if (r - l + 1) > minutes:
                if grumpy[l]:
                    cur_converted -= customers[l]
                l += 1
            if grumpy[r]:
                cur_converted += customers[r]
            max_converted = max(max_converted, cur_converted)

        return num_satisfied + max_converted