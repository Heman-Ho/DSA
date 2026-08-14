class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                # Current element + Top + Left - Top-Left diagonal
                self.dp[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.dp[r][c + 1]
                    + self.dp[r + 1][c]
                    - self.dp[r][c]
                )

    def sumRegion(
        self, row1: int, col1: int, row2: int, col2: int
    ) -> int:
        # Bottom-Right - Top Strip - Left Strip + Top-Left diagonal
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )