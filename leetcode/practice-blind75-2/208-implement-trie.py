class TrieNode:
    children = {}  # 'a' : TrieNode('a')

    def __init__(self, val):
        self.val = val
        self.isEnd = False

    def add_child(self, char):
        if char not in self.children:
            self.children[char] = TrieNode(char)
        return self.children[char]

    def contains_child(self, char):
        if char in self.children:
            return self.children[char]


class Trie:

    def __init__(self):
        self.root = TrieNode("START")

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            node = root.add_child(char)
            root = node
        root.isEnd = True
        return

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True


obj = Trie()
obj.insert("word")
print(obj.search("word"))
print(obj.startsWith("wo"))
