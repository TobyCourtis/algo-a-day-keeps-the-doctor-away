Initial thoughts:
- Decided to pass on attempting a solution straight away due to lack of knowledge in Python pass by assignment

Optimal solution:
NB - Python pass by assignment (full understanding) was vital to this solution

with example l1 = [1,3,4] l2 = [2,5,6]
1. set temporary pointer cur as well as fixed pointer dummy to an empty Node (ListNode())
2. check which list has the lower value at head (list1 as 1 < 2)
3. cur.next (originally the same as dummy.next) is updated to be the whole of list1
4. cur = cur.next (now at the tail of the list)
5. list1 = list1.next (shortening list1 by one node as this has been assigned already)
6. Repeat steps 2 and this time cur.next (tail) is updated to be the whole of list2 
    - This means the global dummy list is now [1,2,5,6]
    - Repeating results in and ordred linked list being formed
7. After loop is finished, append any of list1 or list2 that are left over
8. Return original pointer dummy.next which is the start of our ordered link list

Original assignment "cur = dummy = ListNode()" and later use of "cur.next" and "cur = cur.next" work due to pass by assignment and dummy always keeps track of the original position in memory of the head of our linked list 
