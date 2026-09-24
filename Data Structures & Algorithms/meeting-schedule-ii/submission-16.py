"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # (1,5), (2, 6), (5,10), (10,15), (15, 20), (1, 20)

        intervals.sort(key=lambda x: x.start)
        res = 0
        min_heap = []

        for interval in intervals:
            while min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            
            res = max(res, len(min_heap))

        return res
                