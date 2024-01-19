Initial attempt:
- Seems fairly trivial comparing both sides of the string working towards the middle
  - return False if characters do not match

beat 92% in runtime, 26% in memory

Optimal (space):
1. Loop through the string with two pointers (left and right)
2. If you encounter a non-alphanumeric, increment or decrement left/right respectively
3. Compare characters and return False if they don't match