import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            course = pre[0]
            prerequisite = pre[1]

            indegree[course] += 1
            adj_list[prerequisite].append(course)  # to do pre, we have to go to course

        # find all nodes with no incoming edges (no prerequisites)
        q = collections.deque()
        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)


        # go to all nodes with no prequisites and 'remove them' by reducing the indegree of all of their adjcaent nodes
        # by 1. k
        # if the adjacent node indegree now == 0, then add it to the queue
        # when we finish, if the graph has a loop then we won't visit the nodes in that loop (none have indegree 0)
        # if visited == numCourses then no loops, else there are loops
        visited = 0
        while q:
            visited += 1
            current_course = q.popleft()

            for adj in adj_list[current_course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        return visited == numCourses


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
