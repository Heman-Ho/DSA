class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 1 2 4 
        # 1 3 3
        seats.sort()
        students.sort()

        res = 0
        for seat, student in zip(seats, students):
            res += abs(seat - student)
        
        return res