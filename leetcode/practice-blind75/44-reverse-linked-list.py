# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        d_prev = None

        while head:
            node = ListNode(head.val)
            node.next = d_prev

            d_prev = node
            head = head.next

        return node


dummy = head = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

three.next = four
two.next = three
head.next = two

while head:
    print(head.val)
    head = head.next

print("----")

s = Solution()
out = s.reverseList(dummy)

while out:
    print(out.val)
    out = out.next
