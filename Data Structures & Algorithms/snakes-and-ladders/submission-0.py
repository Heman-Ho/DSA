from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        target = N * N

        def to_rc(s):
            row_from_bottom, offset = divmod(s - 1, N)
            r = N - 1 - row_from_bottom
            c = offset if row_from_bottom % 2 == 0 else N - 1 - offset
            return r, c

        q = deque([(1, 0)])
        seen = {1}

        while q:
            s, turns = q.popleft()
            if s == target:
                return turns
            for step in range(1, 7):
                nxt = s + step
                if nxt > target:
                    break
                r, c = to_rc(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, turns + 1))

        return -1