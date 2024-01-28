Initial thoughts:
- You can climb stairs by taking either a 2 step or a 1 step as a next step
- Base case 1 or 0 return 1 as there was another way of climbing the stairs
- Aggregate of func(n-2) + func(n - 1) .. is the number of unique ways of climbing. Every "Step" results in a return of 1 which is a new way of climbing the stairs
```
 def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
```

First submission beat 94% of users in runtime, 86% memory

Optimal:
- Just cache climbStairs because self.climbStairs(n) is called many times

