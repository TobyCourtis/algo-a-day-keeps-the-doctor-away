# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = set()
        seen.add(hash(head))

        while head.next:
            head = head.next
            hashed = hash(head)
            if hashed in seen:
                return True

            seen.add(hashed)
        return False


# playing with obj hashes
first = ListNode(6)
first.next = ListNode(6)

print(hash(first))
print(hash(first.next))

second = ListNode(6)
second.next = ListNode(6)

print(hash(second))
print(hash(second.next))

obj = "example"
hash_code = hash(obj)
print(hash_code)

obj2 = "example"
print(hash(obj2))

s = Solution()
