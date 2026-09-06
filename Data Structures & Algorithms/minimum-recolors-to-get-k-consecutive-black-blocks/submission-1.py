class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Find a window of size k with the least amount of Ws

        num_W = blocks[:k].count('W')
        best = num_W

        for r in range(k, len(blocks)):
            if blocks[r] == 'W':
                num_W += 1
            if blocks[r-k] == 'W':
                num_W -= 1
            best = min(best, num_W)
        return best