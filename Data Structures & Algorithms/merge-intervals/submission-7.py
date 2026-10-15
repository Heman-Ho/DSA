class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        # [1,3], [2, 4], [4, 6], [7, 9]
        # [[1, 6], [7, 9]]

        res.append(intervals[0])

        for interval in intervals[1:]:
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res