from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head.next:
            if head.val == "SEEN":
                return True
            head.val = "SEEN"
            head = head.next

        return False


s = Solution()
tmp = ListNode(3)
second = ListNode(2)
tmp.next = second
tmp.next.next = ListNode(0)
tmp.next.next.next = ListNode(-4)
tmp.next.next.next.next = second

print(s.hasCycle(tmp))
