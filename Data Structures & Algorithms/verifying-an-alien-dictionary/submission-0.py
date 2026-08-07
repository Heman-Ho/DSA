class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}

        # Convert each word to a tuple of integer ranks: "app" -> (0, 15, 15)
        transformed = [[order_map[c] for c in w] for w in words]

        # Check if transformed list is sorted
        return transformed == sorted(transformed)