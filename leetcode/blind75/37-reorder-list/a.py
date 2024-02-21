# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reorderListAttempOne(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        tmp = head.next
        while tmp:
            stack.append(tmp)
            tmp = tmp.next

        end = True
        current = head
        while stack:
            if end:
                current.next = stack.pop()
            else:
                current.next = stack.pop(0)
            end = not end
            current = current.next

        # make last node point to None
        current.next = None

    def reorderListNeet(self, head: Optional[ListNode]) -> None:
        # 1. half lists
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of list
        second = slow.next  # second is now second half of the list
        slow.next = None  # break first half of list
        prev = None

        # case second = 4,5,6. See reverse logic below
        while second:
            # store rest of list
            tmp = second.next  # tmp = 5, 6     # tmp = 6      # tmp = None

            # make next value = previous values
            second.next = prev  # 4.next = None  # 5.next = 4   # 6.next = 5,4

            # make previous = second (as second has been changed to head -> previous in line above)
            prev = second  # prev = 4       # prev = 5, 4  # prev = 6

            # set second to rest of list
            second = tmp  # second = 5, 6  # second = 6   # second = None

        # merge the two lists
        first = head
        second = prev

        # case first = 1,2,3   second = 4,5,6
        while second:
            tmp1, tmp2 = first.next, second.next  # saved because we will break links at the end
            first.next = second  # 1.next = 6
            second.next = tmp1  # 6.next = 2
            first, second = tmp1, tmp2  # set first and second to their next values we saved earlier
            # first = 2,3  second = 5,4


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
s = Solution()
# s.reorderList(head)
s.reorderListAttempOne(head)
while head:
    print(head.val)
    head = head.next
