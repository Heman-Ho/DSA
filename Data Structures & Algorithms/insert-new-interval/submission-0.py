class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # We can merge overlapping intervals by: 
        # merged_interval[0] = min(interval1[0], interval2[0])
        # merged_interval[1] = max(interval1[1], interval2[1])

        # We can detect overlapping intervals by: 
        # interval1[1] >= interval2[0] and interval1[0] <= interval2[0]
 
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: # newInterval overlaps with the cur interval
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max((intervals[i][1], newInterval[1]))
                ]
        
        res.append(newInterval)
        return res