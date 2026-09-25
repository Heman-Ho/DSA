from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(set)
        
        def isNeighbor(s1, s2):
            num_mismatch = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    num_mismatch += 1
                    if num_mismatch > 1:
                        return False
            return True
        
        for word in wordList:
            if isNeighbor(beginWord, word):
                adj[beginWord].add(word)
        
        for i in range(len(wordList)):
            w1 = wordList[i]
            for j in range(i+1, len(wordList)):
                w2 = wordList[j]
                if isNeighbor(w1, w2):
                    adj[w1].add(w2)
                    adj[w2].add(w1)

        queue = deque()
        queue.append(beginWord)
        seqLen = 1
        visited = set()

        while queue:
            qLen = len(queue)

            for i in range(qLen):
                word = queue.popleft()
                for neighbor in adj[word]:
                    if neighbor == endWord:
                        return seqLen + 1
                    if neighbor not in visited:
                        queue.append(neighbor)
                visited.add(word)

            seqLen += 1
        
        return 0