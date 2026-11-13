class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for wgt in w:
            self.prefix.append(self.prefix[-1] + wgt)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()
        l, r = 1, len(self.prefix)
        while l < r:
            mid = (l + r) >> 1
            if self.prefix[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l - 1