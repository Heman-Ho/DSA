class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [] 
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for cur in intervals[1:]:
            if prev[1] < cur[0]:
                res.append(prev)
                prev = cur
            else:
                prev[1] = max(cur[1], prev[1])
        
        res.append(prev)
        return res

        