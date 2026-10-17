"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        # keep a min heap of end times which keeps hold of intervals that need to be scheduled at the same time
        min_heap = [] 
        res = 0

        # for every interval
        for interval in intervals:
            # while new iterval start time is >= top of min heap, pop from min heap
            while min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval.end)
            res = max(res, len(min_heap))
        
        return res

