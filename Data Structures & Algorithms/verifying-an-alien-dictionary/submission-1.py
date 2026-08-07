class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Step 1: Map each character to its rank (O(1) time since order len = 26)
        order_map = {char: i for i, char in enumerate(order)}

        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Compare characters one by one
            for k in range(len(w1)):
                # If w1 is longer than w2 and all previous chars matched (e.g., "apple" vs "app")
                if k >= len(w2):
                    return False

                if w1[k] != w2[k]:
                    # If first non-matching char in w1 has higher rank than in w2
                    if order_map[w1[k]] > order_map[w2[k]]:
                        return False
                    # Found the first difference and it's in correct order, stop checking this pair!
                    break

        return True