def minFriends(numNodes, numEdges):
    # think of the graph as a straight line of nodes
    # given we have to use all edges, what is the largest minimal size connected group we can make
    # for sample case 2, a connected group of size 2 exists but we have to make a group of size 3 by using all edges, hence output = 3

    # algorithm that should work:
    # 1. define all nodes with edgeCount = 0
    # 2. connect lowest edgeCount node to second lowest edge count node (+1 to both node's edgeCount)
    # 3. repeat step 2 until all edges are used
    # 4. find largest connected graph created
    if numNodes == 1:
        return 1

    nodes = [0] * numNodes

    for i in range(numEdges):
        min_node = nodes.index(min(nodes))
        nodes[min_node] += 1
        next_min_node = nodes.index(min(nodes))
        nodes[next_min_node] += 1

    return max(nodes)


print(minFriends(4, 6))


list_of_sets = [{1, 2}, {2}, {3, 4}, {4, 5}, {5}]

merged_sets_list = []
for s in list_of_sets:
    for ms in merged_sets_list:
        if not s.isdisjoint(ms):
            ms.update(s)
            break
    else:
        merged_sets_list.append(s.copy())

print(merged_sets_list)
