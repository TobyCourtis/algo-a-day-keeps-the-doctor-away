class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def gimme_tree(t):
    if t is None:
        t = TreeNode(10)
    t.val = t.val - 1
    if t.val <= 0:
        return None

    return TreeNode(t.val, left=gimme_tree(t), right=gimme_tree(t))

# print(vars(gimme_tree(None)))


five = TreeNode(5, None, None)
one = TreeNode(1, None, None)
two = TreeNode(2, None, None)
four = TreeNode(4, left=one, right=two)
t1 = TreeNode(3, left=four, right=five)

arr = []
def print_tree(t):
    if t is None:
        return
    print(t.val)
    arr.append(t.val)
    print_tree(t.left)
    print_tree(t.right)


print_tree(t1)
print(arr)
