class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by start time increasing 
        # return how many intervals remain
        intervals.sort(key=lambda x: (x[0], -x[1]))
        num_overlap = 0

        # [0, 8], [2, 8], [6, 10]

        cur_end = 0
        for i in range(len(intervals)):
            if intervals[i][1] <= cur_end:
                num_overlap += 1
            else:
                cur_end = intervals[i][1]
        
        return len(intervals) - num_overlap