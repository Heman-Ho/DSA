class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}
        for i, d in enumerate(digits):
            last[int(d)] = i

        for i, d in enumerate(digits):
            d = int(d)
            # try to place a bigger digit here, biggest first
            for want in range(9, d, -1):
                if last.get(want, -1) > i:
                    j = last[want]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))

        return num