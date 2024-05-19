from typing import (
    List,
)


class Solution:

    def alien_order(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}  # build empty adjacency dict

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                # if abcd comes before abc then invalid (in Leetcode description)
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}  # False=visited, True=in current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]  # this also means if we've done "t" before then we don't re-add t to path (res.append)
                # if we do t -> f then next for loop we do w, visit["t"] will return False and not append to res

            visit[c] = True

            for nbr in adj[c]:
                if dfs(nbr):
                    return True  # detected loop

            visit[c] = False  # now tha path has been built, we can set to False
            res.append(c)

        for c in adj:  # we can start from any point in graph (since we build path by coming back through)
            # case w -> t -> f
            # if we start at t, we append to res 'f' then 't'
            # then we do char w (since this for loop goes through them all) and append w. dfs() returns False as
            # we've already visited t and f (and set them to False)
            # res = [f,t,w] = "wtf" reversed.
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)

    def alien_order_first(self, words: List[str]) -> str:

        rules = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    print(f"{w1[j]} < {w2[j]}")
                    rules.add((w1[j], w2[j]))
                    break

            # if word1 has same start as word 2,
            # increment chars until chars are not equal
            # add rule about char1 < char2

        while True:
            for rule1 in rules:
                for rule2 in rules:
                    if rule1 != rule2:
                        print('do work')

        return ""


s = Solution()
out = s.alien_order(["wrt", "wrf", "er", "ett", "rftt"])
print(out)
assert out == "wertf"
