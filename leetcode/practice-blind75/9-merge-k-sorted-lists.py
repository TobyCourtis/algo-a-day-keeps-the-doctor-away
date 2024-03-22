import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            tmp_lists = []
            for i in range(0, len(lists) - 1, 2):  # start 0, stop len()-1, step = 2
                l1 = lists[i]
                l2 = lists[i + 1]

                merged_list = self.mergeTwoLists(l1, l2)
                tmp_lists.append(merged_list)

            if len(lists) % 2 != 0:
                tmp_lists.append(lists[-1])  # if lists was odd, we haven't merged the final list so append to new list

            lists = tmp_lists

        return lists[-1] if lists else None

    def mergeTwoLists(self, l1, l2):
        cur = dummy = ListNode(0)

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

        if l2:
            cur.next = l2

        return dummy.next


s = Solution()

out = s.mergeKLists(
    [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])

while out:
    print(out.val)
    out = out.next
