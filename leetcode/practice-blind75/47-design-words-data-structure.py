class Node:
    def __init__(self, val, isEnd=False):
        self.val = val
        self.isEnd = isEnd
        self.children = {}  # "a": Node("a")


class WordDictionary:

    def __init__(self):
        self.root = Node("ROOT")

    def addWord(self, word: str) -> None:
        if not word:
            return
        cur_node = self.root
        for char in word:
            node = Node(char)

            if char not in cur_node.children:
                cur_node.children[char] = node
            cur_node = cur_node.children[char]

        cur_node.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(word_index, cur_node):
            cur = cur_node

            for i in range(word_index, len(word)):
                c = word[i]

                if c == ".":
                    for node in cur.children.values():
                        if dfs(i + 1, node):
                            return True
                    return False  # if none of they children resulted in True then return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnd

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("at")
obj.addWord("bat")
print(obj.search("b."))

obj.addWord("bad")
obj.addWord("buy")
param_2 = obj.search(".ad")
assert param_2 == True
param_2 = obj.search("bad")
assert param_2 == True
param_2 = obj.search("foo")
assert param_2 == False

obj.addWord("a")
print(obj.search("aa"))
print(obj.search(".a"))
print(obj.search("a."))
