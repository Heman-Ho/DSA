class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        # Mark the end of the word
        cur['#'] = None

    def search(self, word: str) -> bool:
        # We will perform dfs on each path
        # if there is a '.' we branch out the paths
        cur = self.trie
        def dfs(i, cur):
            if not cur:
                return False
            if i >= len(word):
                return '#' in cur
            c = word[i]
            if c == ".":
                for letter in cur:
                    if letter != "#" and letter != "." and dfs(i + 1, cur[letter]):
                        return True
                return False
            elif c not in cur:
                return False
            else:
                return dfs(i+1, cur[c])

        return dfs(0, cur)
