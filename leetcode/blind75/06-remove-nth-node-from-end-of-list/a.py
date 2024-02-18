# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy

        right = head

        while n > 0 and right is not None:
            right = right.next
            n -= 1

        # now right is correcty set to the (dummy + n) node

        while right is not None:
            left = left.next
            right = right.next

        # now right is null, left is the value before the nth node from the end
        left.next = left.next.next

        return dummy.next


s = Solution()
print(s.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3))), 2).val)
