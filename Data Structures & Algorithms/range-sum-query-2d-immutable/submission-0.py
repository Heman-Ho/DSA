class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.sums = matrix
        
        for i in range(self.ROWS - 1, -1, -1):
            for j in range(self.COLS - 1, -1, -1):
                sum1 = sum2 = sum3 = 0
                if i + 1 < self.ROWS:
                    sum1 = self.sums[i+1][j]
                if j + 1 < self.COLS:
                    sum2 = self.sums[i][j+1]
                if i + 1 < self.ROWS and j + 1 < self.COLS:
                    sum3 = self.sums[i+1][j+1]
                self.sums[i][j] += sum1 + sum2 - sum3


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum1 = self.sums[row1][col1]
        sum2 = sum3 = sum4 = 0
        if col2 + 1 < self.COLS and row2 + 1 < self.ROWS:
            sum4 = self.sums[row2+1][col2+1]

        if col2 + 1 < self.COLS:
            sum2 = self.sums[row1][col2+1]
       
        if row2 + 1 < self.ROWS:
            sum3 = self.sums[row2+1][col1]
      
        return sum1 - sum2 - sum3 + sum4


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 