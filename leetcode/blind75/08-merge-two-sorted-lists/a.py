def print_linked(linked):
    out_string = ""
    while linked.next:
        print(linked.val)
        out_string += str(linked.val) + ", "
        linked = linked.next
    return out_string


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1

                cur = cur.next
                list1 = list1.next

            else:
                cur.next = list2

                cur = cur.next
                list2 = list2.next

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


l1 = ListNode(1, ListNode(3, ListNode(4, None)))
l2 = ListNode(2, ListNode(5, ListNode(6, None)))

s = Solution()
out = s.mergeTwoLists(l1, l2)
print_linked(out)
