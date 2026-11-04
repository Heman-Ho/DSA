class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        latest_end = 0
        res = 0

        for meeting in meetings:
            if meeting[0] > latest_end + 1:
                res += (meeting[0] - latest_end - 1)
            
            latest_end = max(latest_end, meeting[1])
        
        if latest_end < days:
            res += (days - latest_end)

        return res