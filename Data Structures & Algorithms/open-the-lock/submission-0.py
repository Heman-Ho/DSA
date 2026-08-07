from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def generate_neighbors(state):
            print(f"state: {state}")
            res = []
            nums = list(int(digit) for digit in state)
            for i in range(4):
                nums[i] = (nums[i] + 1) % 10
                res.append("".join(str(num) for num in nums))
                nums[i] = (nums[i] - 2) % 10
                res.append("".join(str(num) for num in nums))
                nums[i] = (nums[i] + 1) % 10
            return res

        # First map the problem to a graph
        # each 4 digit combo => node
        # 8 edges out of each node (turn any of the 4 wheels one of 2 directions)
        # Constraints: cannot step out of a lock state
        visited = set(deadends)

        if "0000" in visited:
            return -1
        
        q = deque([("0000", 0)])
        visited.add("0000")

        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            
            for neighbor in generate_neighbors(state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, turns + 1))
        
        return -1

