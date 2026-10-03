class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]] 
        
        for cur in intervals[1:]:
            if res[-1][1] < cur[0]:
                res.append(cur)
            else:
                res[-1][1] = max(res[-1][1], cur[1])
        
        return res

        