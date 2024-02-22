Attempt:

This is house robber 1 problem with additonal constraints.

- We can only rob final house if we haven't used house1

and vice versa:

- We can only rob first house if we haven't used final house

The problem can be solved reusing robber1 function:

We pass array with either:

1. all values except final house OR
2. all values except first house

This is because intuitively, we cannot use both so we compute one solution with, one without.



NB - if we try to solve it all at once and get to the end of the array, we cannot just append the max(firstHouse, lastHouse) as the decision of which house from the start of the problem affects every other decision of which houses to rob.

e.g if we rob house[1], compute all other houses then get to house[-1], we cannot just use house[-1] and subtract house[1], we need to recompute the entire problem


Runtime beat 78%, memory 89%