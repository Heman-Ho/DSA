from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R_queue = deque()
        D_queue = deque()

        for i, senate in enumerate(senate):
            if senate == "R":
                R_queue.append(i)
            else:
                D_queue.append(i)
        
        while R_queue and D_queue:
            R_turn = R_queue.popleft()
            D_turn = D_queue.popleft()
            # Case: senate from R party's turn
            if R_turn < D_turn:
                R_queue.append(R_turn + n)
            else:
                D_queue.append(D_turn + n)
        
        return "Dire" if D_queue else "Radiant"