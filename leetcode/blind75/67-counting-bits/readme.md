Trivial enough on first attempt

First submission beat 72% in runtime and 34% memory.

Second submission only beat 10% runtime, 10% memory (not good).
    - The attempt here was to find the largest X where 2 ^ X goes into i
    - From here do i - 2^X and repeat until i == 0
    - The number of times you do this process is the number of 1s in the binary representation

    Open thoughts on solution 2 - we compute the same numbers many times. Let's try cache this in a dict.


Cache:
- Beat 5% runtime, 15% memory.
- I believe because most numbers are not cached this method is still not performant



Optimal:
- Bitshifting - see optimal.py
- In the end fairly trivial leveraging caching and logical operations
- Caching in my original attempt was close but overly complex


