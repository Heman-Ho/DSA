class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_tens = 0
        num_fives = 0
        for bill in bills:
            if bill == 5:
                num_fives += 1
            if bill == 10:
                # You must return a 5
                if num_fives == 0:
                    return False
                num_fives -= 1
                num_tens += 1
            if bill == 20:
                # either return 10 + 5 or 5 + 5 + 5
                if num_tens > 0 and num_fives > 0:
                    num_tens -= 1
                    num_fives -= 1
                elif num_fives >=3:
                    num_fives -=3
                else:
                    return False
        return True