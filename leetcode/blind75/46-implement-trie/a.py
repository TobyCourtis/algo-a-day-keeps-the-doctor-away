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


class Trie:

    def __init__(self):
        self.root = {str: TrieNode}

    def insert(self, word: str) -> None:
        depth = 1

        if word[0] in self.root:
            cur = self.root[word[0]]

            while word[depth] in cur.children:
                cur = cur.children[word[depth]]
                if depth == len(word) - 1:
                    cur.isEnd = True
                    return
                depth += 1
        else:
            cur = TrieNode(word[0])
            self.root[cur.val] = cur

        for i in range(depth, len(word)):
            node = TrieNode(word[i])
            cur.addSibling(node)
            cur = node

        cur.isEnd = True

    def search(self, word: str) -> bool:
        if word[0] not in self.root:
            return False

        cur = self.root[word[0]]

        for i in range(1, len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]

        return True if cur.isEnd is True else False

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.root:
            return False

        cur = self.root[prefix[0]]

        for i in range(1, len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]

        return True


class TrieNode:

    def __init__(self, val, isEnd=False):
        self.val = val
        self.isEnd = isEnd
        self.children = {}

    def addSibling(self, node):
        self.children[node.val] = node


word = 'apple'
obj = Trie()
obj.insert(word)
print(obj.search(word))
print(obj.startsWith('app'))
print(obj.search('app'))

obj.insert('app')
print(obj.search('app'))
