import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spells:  [1, 2, 3]
        # potions: [2, 4, 2]
        # success = 5

        def bin_search(spell: int) -> int:
            l, r = 0, len(potions) - 1

            # edge case where no search window exists
            if potions[0] * spell < success:
                return 0

            while l < r:
                m = math.ceil((l + r) / 2)
                if spell * potions[m] < success:
                    r = m - 1 # use a larger potion
                else:
                    l = m # converge to smallest potion that is successful
            
            return l + 1 # number of potions that can mix with spell to be stronger or equal to success

        res = [0] * len(spells)

        # sort potions descending order
        potions.sort(reverse=True)

        # for every spell
        for i, spell in enumerate(spells):
            # use binary serach to find the smallest potion that is successful and add that to res
            res[i] = bin_search(spell)
        
        return res
