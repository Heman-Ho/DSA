import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Greediliy choose the lowest number in hand to be the start of a new straight
        counts = Counter(hand)
        min_heap = []
        for num, count in counts.items():
            min_heap.append((num, count))
        heapq.heapify(min_heap)

        while min_heap:
            prev = -1
            buffer = []

            for _ in range(groupSize):
                if not min_heap:
                    return False

                card, count = heapq.heappop(min_heap)
                # print(f"popping {card}, {count}")
                if prev != -1 and card != prev + 1:
                    return False
                if count > 1:
                    buffer.append((card, count-1))
                prev = card
            for item in buffer:
                heapq.heappush(min_heap, item)
                # print(f"pushing {item}")
        
        return True