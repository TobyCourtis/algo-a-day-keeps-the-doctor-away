Initial thoughts:

Submission:
Beat 98.8% runtime, 80% memory

(assuming node.val values are unique)
1. seen = set()
2. add head.val to seen
3. head = head.next
4. if head.val in seen: return True (cycle exists)
5. If we go through the whole list with no cycle, return False

Changes (node.val values were not unique):

- Change step 2 to append `hash(head)` (unique for each node) instead of just head.val (which was not unique)

<br>

Optimal:

Mine was optimal in runtime


For memory:

- We would not have to keep a "seen" set if instead we changes the value of head.val for each node we saw to "0.5" (a unique number).
- If we later encounter value 0.5 as head.val then we've looped! (return True).
- If we reach end of list, head.next will equal None so return False