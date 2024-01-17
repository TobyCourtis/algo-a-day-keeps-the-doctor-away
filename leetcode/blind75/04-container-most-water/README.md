Overview:

Approach taken worked and passed 51/62 test cases.

Longer test cases failed due to time limit exceeded.

Issue is time complexity of O(n^2)


Optimal:

I should have spotted the two pointer method (O(n)):
- Begin with first and last elem in list
- Compute max_area
- Move the pointer left + 1 if left is shortest height or right - 1 if right is shortest height
- Compute max_area
- Continue until the pointers meet