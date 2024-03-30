# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy  # left one before right
        right = head

        while n > 0 and right is not None:
            n -= 1
            right = right.next

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


s = Solution()
out = s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
print(out)
while out:
    print(out.val)
    out = out.next
