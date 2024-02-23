Neetcode (dynamic programming):

Intuitive, work backwards through array logging longest sequence at each index

1. init all DP values to 1:    `DP = [1] * len(nums)`
2. loop backwards through nums
   3. At each index, DP[index] = max(1, DP[index + 1], ... , DP[index == n - 1])
   4. We can only use a previously calculated DP value if nums[index] < nums[index + x]
   5. Case [1,2,4,0]
   6. DP[2] = max(1, DP[3]). Since nums[3] = 0, we cannot use DP[3] therefore max = 1
      7. DP[2] = 1
3. return max(DP)

O(n log n) solution out of scope. 

Could not evaluate solution as it's leetcode premium problem