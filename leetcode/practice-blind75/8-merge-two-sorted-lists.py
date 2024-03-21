class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur = dummy = ListNode(0)

        while list1 and list2:
            if list2.val < list1.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next


s = Solution()
out = s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))),
                      ListNode(1, ListNode(3, ListNode(4))))
while out:
    print(out.val)
    out = out.next
