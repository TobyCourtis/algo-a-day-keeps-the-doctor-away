Attempt:

RTFQ - The problem was to remove the nth from the END of the list not the start.

Could reverse the list and then remove len(list) - n. Not the most efficient way.

<br>

1. Make initial dummy node 0
2. set left to 0
3. set right to nth node
4. Repeat in loop:
    5. left node = left.next
    6. rigth node = right.next
    5. Walk through list until right node is set to None (goes off the end of the list)
5. Now we know that left is the node before the nth node from the end.
6. set left.next = left.next.next (skipping the nth node from the end and thus removing it from the list)
7. return dummy_node.next at the end

Runtime beat 49%, memory 73%