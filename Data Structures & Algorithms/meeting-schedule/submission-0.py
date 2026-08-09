"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        # Sort the intervals by the start time
        intervals.sort(key=lambda x: x.start)

        # Loop through intervals
        for i in range(1, len(intervals)):
            # if interval's start time is before the previous interval's end time: return False
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True