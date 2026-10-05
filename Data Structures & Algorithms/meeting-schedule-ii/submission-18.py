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
        # sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        res = 0
        
        # Use a min heap of end times
        min_heap = []

        for interval in intervals:
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            res = max(res, len(min_heap))

        return res