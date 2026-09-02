import heapq, math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)

        for _ in range(k):
            largest_pile = -heapq.heappop(gifts)
            gifts_remain = int(math.sqrt(largest_pile))
            heapq.heappush(gifts, -gifts_remain)
        return -sum(gifts)