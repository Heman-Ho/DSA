class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        counts = defaultdict(int)
        max_count = 0 

        for row in wall:
            for i in range(len(row) - 1):
                if i > 0:
                    row[i] += row[i-1]
                counts[row[i]] += 1

                max_count = max(max_count, counts[row[i]])
        
        return len(wall) - max_count

        
