Initial thoughts:
- Very easy problem to run into a O(n^2) approach (see maxProfitONSquared())
- Second approach O(n) is trivial enough
  - loop through once
  - set initial buy to first day
  - if a price is found lower than the initial buy then set that to min buy
  - update max profit if current - min > maxProfit

Runtime beat 94% users, memory 82%