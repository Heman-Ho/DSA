class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Difference array representing passenger delta at each kilometer marker
        delta = [0] * 1001

        for passengers, start, end in trips:
            delta[start] += passengers  # Boarding
            delta[end] -= passengers  # Disembarking

        curr_passengers = 0
        for change in delta:
            curr_passengers += change
            if curr_passengers > capacity:
                return False

        return True