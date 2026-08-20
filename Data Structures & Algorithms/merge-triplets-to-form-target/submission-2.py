class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        completed = [False] * 3
        num_completed = 0
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
          
            for i in range(3):
                if not completed[i] and triplet[i] == target[i]:
                    completed[i] = True
                    num_completed += 1
                    if num_completed == 3:
                        return True
        return False
        
        
            