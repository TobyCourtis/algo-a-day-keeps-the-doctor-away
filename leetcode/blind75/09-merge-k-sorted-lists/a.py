# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return

        while len(lists) > 1:
            tmp = []

            midpoint = len(lists) // 2
            for i in range(midpoint):
                l1 = lists[i]
                l2 = lists[midpoint + i]
                merged = self.mergeTwoLists(l1, l2)

                tmp.append(merged)

            if len(lists) % 2 != 0:  # if odd then add the last element which wasn't merged
                tmp.append(lists[-1])

            lists = tmp

        return lists[0]

    def mergeTwoLists(self, l1, l2) -> Optional[ListNode]:  # answer to 08 'merge 2 sorted lists' problem
        # create start node
        cur = head = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return head.next


s = Solution()
out = s.mergeKLists([ListNode(1, ListNode(5)), ListNode(3, ListNode(4))])
while out:
    print(out.val)
    out = out.next


# out = s.mergeTwoLists(ListNode(1, ListNode(5)), ListNode(2, ListNode(6)))
# print(out.val)
# print(out.next.val)
