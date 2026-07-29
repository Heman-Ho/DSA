class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Let dp[i,j] = the number of uique paths to reach obstacleGrid[i,j]
        # If there is an obstacle => 0 unique paths to reach that location
        # dp[i,j] = dp[i-1,j], dp[i,j-1]

        # Assumption: I am allowed to modify the obstacleGrid input

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        # Update the first row and col of the grid
        obstacleGrid[0][0] = 1

        for r in range(1, ROWS):
            if obstacleGrid[r][0] == 1:
                obstacleGrid[r][0] = 0
            else:
                obstacleGrid[r][0] = obstacleGrid[r-1][0]

        for c in range(1, COLS):
            if obstacleGrid[0][c] == 1:
                obstacleGrid[0][c] = 0
            else:
                obstacleGrid[0][c] = obstacleGrid[0][c-1]

        for r in range(1,ROWS):
            for c in range(1,COLS):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]

        return obstacleGrid[ROWS-1][COLS-1]
