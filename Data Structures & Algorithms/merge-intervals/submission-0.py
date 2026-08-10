class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            # Case 1: the cur_interval doesn't overlap with the new_interval
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                new_interval = intervals[i]
            # Case 2: the interval overlaps with the new_interval
            else:
                new_interval = [
                    min(new_interval[0], intervals[i][0]),
                    max(new_interval[1], intervals[i][1])
                ]
        res.append(new_interval)
        return res