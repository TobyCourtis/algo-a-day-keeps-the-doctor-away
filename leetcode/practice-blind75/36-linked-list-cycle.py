from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    """
    Constant memory
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        while head.next:
            if head.val == 0.5:
                return True
            head.val = 0.5
            head = head.next

        return False

    """
    Best runtime
    """
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head.next:
            if head.val in visited:
                return True
            visited.add(head.val)
            head = head.next

        return False


s = Solution()
root = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

root.next = two
two.next = three
three.next = two

print(s.hasCycle(root))
root.next = four
print(s.hasCycle(root))
