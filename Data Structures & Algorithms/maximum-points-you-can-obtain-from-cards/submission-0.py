class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # [1, 2, 6, 3, 2, 1, 5]
        #l           r
        # cur_sum = 7
        cur_sum = sum(cardPoints[:k])
        res = cur_sum
        l = k - 1

        for r in range(len(cardPoints) - 1, len(cardPoints) - k - 1, -1):
            cur_sum -= cardPoints[l]
            cur_sum += cardPoints[r]
            l -= 1
            res = max(res, cur_sum)
        return res