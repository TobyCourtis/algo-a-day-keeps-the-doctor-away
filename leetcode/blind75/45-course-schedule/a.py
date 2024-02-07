from collections import defaultdict, deque


class Solution:
    cache = {}

    def canFinishOne(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        dependency_dict = defaultdict(list)

        for pre in prerequisites:
            if pre[0] == pre[1]:
                return False
            dependency_dict[pre[0]].append(pre[1])

        changed = True
        while changed and len(dependency_dict.items()) > 1:
            to_del = []
            changed = False

            # 1. iter dictionary of prerequisites
            for k, prereq in dependency_dict.items():
                if not prereq:
                    to_del.append(k)
                    continue

                pruned_reqs = []  # build up new list of preeqs

                # go through current key's prequisites and remove them if not in dictionary or value = []
                # value will equal [] in the case that we've removed all elements this loop
                for req in prereq:
                    if req not in dependency_dict or dependency_dict[req] == []:
                        changed = True
                    else:
                        pruned_reqs.append(req)

                dependency_dict[k] = pruned_reqs

            # drop all keys with value == []
            for k in to_del:
                del dependency_dict[k]

        return len(dependency_dict.keys()) <= 1

    def canFinishTwo(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        dependency_dict = defaultdict(list)

        for key in range(0, numCourses + 1):
            dependency_dict[key]

        for pre in prerequisites:
            if pre[0] == pre[1]:
                return False
            dependency_dict[pre[0]].append(pre[1])

        changed = True
        while changed:
            changed = False

            # 1. iter dictionary of prerequisites
            for k, prereq in dependency_dict.items():
                if not prereq:
                    continue

                pruned_reqs = []  # build up new list of preeqs

                # go through current key's prequisites and remove them if not in value = [] (no dependencies)
                for req in prereq:
                    if not dependency_dict[req]:  # if == []
                        changed = True
                    else:
                        pruned_reqs.append(req)

                dependency_dict[k] = pruned_reqs

        return len([key for key, value in dependency_dict.items() if value != []]) <= 1

    def canFinishRecursive(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        dependency_dict = defaultdict(list)

        for key in range(0, numCourses + 1):
            dependency_dict[key]

        for pre in prerequisites:
            if pre[0] == pre[1]:
                return False
            dependency_dict[pre[0]].append(pre[1])

        return all([self.solvable(k, None, dependency_dict) for k in dependency_dict.keys()])

    def solvable(self, k_original, new_key, dictionary):
        if new_key == k_original:  # we have a loop so not possible
            return False

        if new_key is None:
            new_key = k_original

        if not dictionary[new_key]:  # == []
            return True

        return all([self.solvable(k_original, prereq, dictionary) for prereq in dictionary[new_key]])

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. create graph of all nodes with incoming edges
        # [1, 3] to do course 1 we have preequisite 3
        # indegree = [0, 1, 0, 0]
        # adjacent = [[], [], [], [1]]
        indegree = [0] * numCourses
        adjacenct_nodes = [[] for x in range(numCourses)]  # e.g index X is a list of all nodes X is a prereq to

        for pre in prerequisites:
            course = pre[0]
            prerequisite_course = pre[1]

            indegree[course] += 1
            adjacenct_nodes[prerequisite_course].append(course)

        q = deque()  # queue of nodes with indegree 0
        # initial populate
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        # we to find each node with degree 0
        visited = 0
        while q:
            visited +=1
            # visit items in queue
            current_node = q.popleft()
            for adj in adjacenct_nodes[current_node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)



        return numCourses == visited


s = Solution()
print(s.canFinish(numCourses=4, prerequisites=[[1, 3]]))


print(s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
print(s.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(s.canFinish(numCourses=1, prerequisites=[]))
print(s.canFinishOne(numCourses=1, prerequisites=[[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
print(s.canFinishOne(numCourses=1, prerequisites=[[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
