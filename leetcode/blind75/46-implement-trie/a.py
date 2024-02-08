class TrieOne:

    def __init__(self):
        self.words = set()
        self.substrings = set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)):
            self.substrings.add(word[0:i + 1])

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.substrings


0
