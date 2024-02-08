# mine was optimal, this is essentially a cleaner approach:

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


class TrieNode:

    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = {}


word = 'apple'
obj = Trie()
obj.insert(word)
print(obj.search(word))
print(obj.startsWith('app'))
print(obj.search('app'))

obj.insert('app')
print(obj.search('app'))
