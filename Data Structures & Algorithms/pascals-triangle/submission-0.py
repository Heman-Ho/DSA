class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for row in range(1, numRows):
            prev_row = res[-1]
            new_row = [0] * (row + 1)
            for i in range(len(new_row)):
                top_left = prev_row[i - 1] if i - 1 >= 0 else 0
                top_right = prev_row[i] if i < len(prev_row) else 0
                new_row[i] = top_left + top_right
            res.append(new_row)

        return res