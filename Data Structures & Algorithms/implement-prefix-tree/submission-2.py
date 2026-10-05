class PrefixTree:

    def __init__(self):
        self.trie = {}
        self.words = set()

    def insert(self, word: str) -> None:
        if self.search(word):
            return

        self.words.add(word)
        cur = self.trie
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur['#'] = '#'
        return


    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True
        