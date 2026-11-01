class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = 0
        cur_time = 0
        for arrival_time, cook_time in customers:
            cur_time = max(cur_time, arrival_time) + cook_time
            waiting_time += cur_time - arrival_time
        
        return waiting_time / len(customers)

        # cur_time = 11
        # waiting_time = 8