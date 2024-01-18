Trivial. Use of set makes this O(n) as each lookup is O(1) after initial conversion.

Runtime beat 87% of users, memory beat 5% users.

Thoughts to avoid high memory use:
- Keep nums as a list (takes a hit of higher time complexity)

Optimal:
- Involves bit manipulation which I will return to later