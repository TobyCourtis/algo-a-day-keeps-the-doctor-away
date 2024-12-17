from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        prev = None

        while head:
            node = ListNode(head.val)
            node.next = prev

            prev = node
            head = head.next

        return node


s = Solution()
print(s.reverseList(ListNode()))
