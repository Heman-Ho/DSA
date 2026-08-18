from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # We use a queue to hold the indices that we can jump to 
        # Keep track of a max_reach variable 
        visited = 0
        q = deque([0])

        while(q):
            index = q.popleft()

            # make the start index at least max_reached to avoid duplicate work
            start = max(visited + 1, index + minJump)
            end = min(index + maxJump, len(s) - 1)
            
            # Add all the possible places we can jump to to the queue
            for i in range(start, end + 1):
                if s[i] == "0":
                    if i == len(s) - 1:
                        return True
                    q.append(i)
            
            visited = max(visited, end)
                
        return False
                    