import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times.sort(key=lambda x: x[0])

        occupied = []        # min-heap of (leave_time, chair_id)
        available = []       # min-heap of free chair ids
        next_chair = 0       # smallest chair number never allocated yet

        for start, end in times:
            while occupied and occupied[0][0] <= start:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)

            # Pick smallest free chair, or allocate a new one
            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            if start == target_arrival:
                return chair

            heapq.heappush(occupied, (end, chair))