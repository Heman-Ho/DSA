class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        # Edge cases: 
        if not board:
            return []

        def dfs(r, c):
            # Base Case
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != "O"):
                return

            # Mark the grid with '#' to represent that it connects to the edge
            board[r][c] = '#'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        # Run a dfs on all the edge cells if it is a O
        # mark all of them with '#' to represent that it's connected to the edge
        # All other Os in the board get surrounded
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(1, COLS - 1):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        # Loop through the board and replace Os with Xs and #s with Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
        

