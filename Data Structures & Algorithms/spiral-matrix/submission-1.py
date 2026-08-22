class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] 
        directions = [(0, 1, 0), (1, 0, 1), (0, -1, 0), (-1, 0, 1)] # delta x, delta y, horizontal/vert
        steps = [len(matrix[0]), len(matrix)] # steps[0] is horizontal steps, # steps[1] is vertical
        loc = [0, -1]

        # 2
        # 0

        while steps[0] > 0 and steps[1] > 0:
            for x, y, d in directions:
                if steps[d] == 0:
                    break
                for _ in range(steps[d]):
                    loc[0] += x
                    loc[1] += y
                    res.append(matrix[loc[0]][loc[1]])
                steps[(d + 1) % 2] -= 1
            
        
        return res