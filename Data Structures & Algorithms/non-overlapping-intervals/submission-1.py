class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1    2    3    4    5    6    7
        # |----|----|----|----|----|----|        
        # |=========|
        #      |=========|
        # |====|

        # We want to maximize the number of intervals to use
        # Greedily choose the intervals with earliest end time to maximize number of intervals used
        intervals.sort(key=lambda x: x[1])

        latest_end_time = float('-inf')
        intervals_used = 0
        for interval in intervals:
            if interval[0] >= latest_end_time:
                intervals_used += 1
                latest_end_time = interval[1]
        
        return len(intervals) - intervals_used