from typing import (
    List,
)


class Graph:

    def __init__(self):
        self.nodes = set()


class Node:

    def __init__(self, val: str):
        self.val = val
        self.neighbours = set()


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:  # topological sort
        # 1. build graph_adj
        # 2. if loop then there's a contradiction
        rules = set()

        prev = words[0]
        for i in range(1, len(words)):
            index = 0
            cur = words[i]
            while prev[index] == cur[index]:
                index += 1
            rules.add((prev[index], cur[index]))
            prev = cur

        graph_adj = {}
        for rule in rules:
            if rule[0] not in graph_adj:
                graph_adj[rule[0]] = set()
            if rule[1] not in graph_adj:
                graph_adj[rule[1]] = set()

            graph_adj[rule[0]].add(rule[1])

        visit = {}
        res = []

        def dfs(c: str):
            if c in visit:
                return visit[c]

            visit[c] = True

            for nbr in graph_adj[c]:
                if dfs(nbr):
                    return True  # detected loop, return and return "" as result

            visit[c] = False
            res.append(c)

        for c in graph_adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)


s = Solution()
print(s.alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
