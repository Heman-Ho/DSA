from collections import defaultdict, deque
from typing import List


class Solution:

    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        # 1. Build adjacency through generic wildcard patterns: O(N * L^2)
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_map[pattern].append(word)

        # 2. BFS initialization
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, length = queue.popleft()

            # Check all intermediate patterns for current_word
            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]

                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return length + 1

                    if neighbor not in visited:
                        visited.add(
                            neighbor
                        )
                        queue.append((neighbor, length + 1))

                # Clear pattern bucket so we never re-evaluate these words from another branch
                pattern_map[pattern] = []

        return 0