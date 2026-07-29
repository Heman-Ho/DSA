import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a mapping of distances to coordinates
        # sort distances 
        # return the first k
        if k >= len(points):
            return points

        distance_to_coord = {}
        distances = []
        for x, y in points:
            distance = x*x + y*y
            if distance not in distance_to_coord:
                distance_to_coord[distance] = []
            distance_to_coord[distance].append([x,y])
            distances.append(distance)
        
        distances.sort()
        print(distances)
        print(distance_to_coord)
        res = []
        for i in range(k):
            res.append(distance_to_coord[distances[i]].pop())
        return res