class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            # Case interval is not overlapping with previous interval
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1]) 
        
        return res