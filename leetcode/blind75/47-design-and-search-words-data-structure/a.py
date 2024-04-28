class Node:

    def __init__(self, val: str, isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd
        # may need isEnd=False

    def add_child(self, char):
        if char not in self.children:
            self.children[char] = Node(char)
        return self.children[char]


class WordDictionary:

    def __init__(self):
        self.root = Node("ROOT")

    def addWord(self, word: str) -> None:
        if not word:
            return

        prev = self.root
        for char in word:
            cur = prev.add_child(char)
            prev = cur
        prev.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    # iterate through all children of current
                    for child in cur.children.values():
                        # call dfs for remaining word and current child e.g (+1, "a"), (+1, "b") etc ..
                        if dfs(i + 1, child):
                            return True
                    return False  # if all children return false for rest of word existing, return False
                else:
                    # generic case, is current char in current children? If not, return False
                    if c not in cur.children:
                        return False
                    # return children of the node matching current character
                    cur = cur.children[c]

            return cur.isEnd

        return dfs(0, self.root)

    def searchFirstAttempt(self, word: str) -> bool:
        possible_nodes = self.root.children.values()

        for i in range(len(word)):
            match = False
            next_possible = []
            for node in possible_nodes:
                if word[i] == '.':
                    next_possible += node.children.values()
                    if i == len(word) - 1:
                        if node.isEnd:
                            match = True
                    else:
                        match = True
                elif word[i] == node.val:
                    if i == len(word) - 1:
                        if not node.isEnd:
                            return False
                    next_possible += node.children.values()
                    match = True

            possible_nodes = next_possible
            if not match:
                return False

        return True


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

word = "bad"
obj.addWord(word)

param_2 = obj.search("bad")
print(param_2)

param_2 = obj.search("..d")
print(param_2)

obj.addWord("lvl")
print(obj.search("..l"))
# param_2 = obj.search("b..")
# print(param_2)
#
# param_2 = obj.search(".ad")
# print(param_2)
#
# param_2 = obj.search(".ag")
# print(param_2)
#
# param_2 = obj.search(".e")
# print(param_2)


# words = ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search",
#          "search", "search", "search", "search", "search"]
# for word in words:
#     obj.addWord(word)
