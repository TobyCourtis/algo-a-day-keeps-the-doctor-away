class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    """
    Best solution is:

    1. split list in half using slow/fast pointer, slow moves forward one and fast moves two

    2. Reverse second half of list (need to revise reversing linked list)

    3. Merge the two lists

    (easy)
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        root = head
        root = root.next
        stack = []
        while root:
            stack.append(root.val)
            root = root.next

        root = head
        while stack:
            root.next = ListNode(stack.pop(-1))
            root = root.next

            if stack:
                root.next = ListNode(stack.pop(0))
                root = root.next

        print(head)
        print(head.next)
