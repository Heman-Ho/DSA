"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, 0))
        
        # Make sure to have end intervals first before start intervals in case of same time
        times.sort()

        cur_rooms = 0
        max_rooms = 0

        for time, state in times:
            # Case: if we are at the start of an interval
            if state == 1:
                cur_rooms += 1
                max_rooms = max(max_rooms, cur_rooms)
            # Case: we are at the end of an interval
            else:
                cur_rooms -= 1
        
        return max_rooms