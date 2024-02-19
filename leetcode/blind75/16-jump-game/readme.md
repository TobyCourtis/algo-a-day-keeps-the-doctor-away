Attempt 1 (canJumpFirstAttempt()):

General approach - recusrively call canJumpFirst for every step (next element) we can take given the current step size.

Example [2, 3, 1, 1, 4]:

- For first element '2' recursively take:
  - 1 step
    - 3 steps (reach last element and return True)
  - 2 steps
    - 1 step 
      - 1 step (reach last element)

<br>

Time limit exceeded. For large use cases there will be a lot of repeated computation (leading to attempt 2)

<br>

Attempt 2 (canJumpSecondAttempt()):

First approach but in reverse.

Produce list of True/False values for if we can or cannot reach the final element for each element in the input array. 

2. Final element = True (we're at the final element)
2. for the ith element, we see if any value is True within the next "x" steps (where x is nums[i] value)
   3. E.g if we're penultimate element of size 1 then we set value to True because we can reach final elem
3. We return True if there is a "True" value in our array within nums[0] elements from the start.


Runtime beat 5%, memory 94%

<br>

Attempt 3 (Neetcode canJump()):

- Similar approach to attempt 2, but we shift the end goal (which starts as last elem) backwards if we can reach an element nearer to the start
- If penultimate element is GT or equal to 1 then we move the end to the penultimate element.
- Repeat for every elem in nums list in reverse.
- If goal index == 0 return True else False (because we couldn't reach the end)

Runtime beat 80%, memory 94%

