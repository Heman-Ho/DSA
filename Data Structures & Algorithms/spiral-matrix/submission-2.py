class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        res = []

        while l <= r or t <= b:
            # top left to top right
            for col in range(l, r + 1):
                res.append(matrix[t][col])
            t += 1
            if t > b:
                return res

            # top right to bottom right
            for row in range(t, b + 1):
                res.append(matrix[row][r])
            r -= 1
            if r < l:
                return res

            # bottom right to bottom left
            for col in range(r, l-1, -1):
                res.append(matrix[b][col])
            b -= 1
            if b < t:
                return res

            # bottom left to top left
            for row in range(b, t-1, -1):
                res.append(matrix[row][l])
            l += 1
            if l > r:
                return res

        return res

        # 1  2  3  4
        # 5  6  7  8 
        # 9 10 11 12

        # res = 1 2 3 4 8 12 11 10 9 5 6 7
        t = 2
        b = 1
        l = 1
        r = 2

