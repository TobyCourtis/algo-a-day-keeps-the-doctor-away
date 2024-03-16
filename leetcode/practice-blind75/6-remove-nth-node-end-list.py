class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = dummy = ListNode(0, head)
        right = head
        for i in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


head = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  ListNode(4))))
# head = ListNode(1)

s = Solution()
out = s.removeNthFromEnd(head, 1)
while out:
    print(out.val)
    out = out.next
