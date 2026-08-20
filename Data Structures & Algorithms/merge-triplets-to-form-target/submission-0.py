class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        completed = [False] * 3
        num_completed = 0
        for triplet in triplets:
            can_use = True
            for i in range(3): 
                if triplet[i] > target[i]:
                    can_use = False
                    break
            if can_use:
                for i in range(3):
                    if not completed[i] and triplet[i] == target[i]:
                        completed[i] = True
                        num_completed += 1
                        if num_completed == 3:
                            return True
        return False
        
        
            