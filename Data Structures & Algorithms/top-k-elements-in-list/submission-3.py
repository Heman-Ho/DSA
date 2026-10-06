from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        # get the counts of each number
        counts = Counter(nums)

        # create a list of tuples (freq, num)
        tuples = [(-freq, num) for num, freq in counts.items()]

        # heapify
        heapq.heapify(tuples)

        # heappop k times to build the output array
        for _ in range(k):
            res.append(heapq.heappop(tuples)[1])
        return res
        # O(klogn)