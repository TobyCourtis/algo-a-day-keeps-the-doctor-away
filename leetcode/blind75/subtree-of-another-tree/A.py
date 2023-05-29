class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


five = TreeNode(5, None, None)
one = TreeNode(1, None, None)
two = TreeNode(2, None, None)
four = TreeNode(4, left=one, right=two)
main_tree_in = TreeNode(3, left=four, right=five)

one_another = TreeNode(1, None, None)
two_another = TreeNode(2, None, None)
sub_tree_in = TreeNode(4, left=one_another, right=two_another)


def find_nodes(t, arr=[]):
    if t is None:
        return
    arr.append(t)

    find_nodes(t.left, arr)
    find_nodes(t.right, arr)
    return arr


def tree_equivalence(main_tree, sub_tree):
    # base case(s)
    if sub_tree is None and main_tree is None:
        return
    elif sub_tree is None or main_tree is None:
        return False

    if sub_tree.val == main_tree.val:
        tree_equivalence(main_tree.left, sub_tree.left)
        tree_equivalence(main_tree.right, sub_tree.right)
    else:
        return False


# Find all nodes of input tree
all_nodes = find_nodes(main_tree_in)

print("\nEquivalent check:")
for match_node in all_nodes:
    if tree_equivalence(match_node, sub_tree_in) is None:
        print("Found match")
    else:
        print("no match")
