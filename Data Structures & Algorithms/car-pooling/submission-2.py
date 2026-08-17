import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        min_heap = []
        # sort trips by the start_loc
        trips.sort(key=lambda x: x[1])

        # at each start_loc:
        for passengers_entering, start_loc, end_loc in trips:
            # 1. while start_loc >= min_heap[0], pop from the heap and increase capacity by the num 
            #    of passengers getting dropped off. 
            while min_heap and start_loc >= min_heap[0][0]:
                _, passengers_exiting = heapq.heappop(min_heap)
                capacity += passengers_exiting

            # 2. pick up all the passengers (if not possible return False)
            if passengers_entering > capacity:
                return False
            
            capacity -= passengers_entering

            # add a tuple (end_loc, num_passengers) to the min heap
            heapq.heappush(min_heap, (end_loc, passengers_entering))
        
        return True