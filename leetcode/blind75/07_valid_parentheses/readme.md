Original solution I attempted was to recursively split down the middle

Correct approach is simple:
1. Create stack
2. Loop through input string
3. if left bracket then push to stack
4. if right bracket then element on top of stack should be a matching left bracket
5. If empty stack at the end and no errors then return True
 
All other edge cases such as a stack that is not empty or trying to pop() empty stack should return False