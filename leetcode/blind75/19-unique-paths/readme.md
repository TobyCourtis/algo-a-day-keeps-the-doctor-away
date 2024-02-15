Attempt:

Idea was to back track from the end node matrix[m - 1][n - 1].

1. Back track through matrix after setting matrix[m - 1][n - 1] = 1
2. matrix[i][j] = right + down
3. end return matrix[0][0]

Runtime beat 50%, memory beat 90%


Optimal:

We do not need to do bottom and right row/column because they are all equal to one.

Rather than slowly initialising matrix, we only need to look at the row below the current row.

Example:

Bottom row = prev_row = [1] * n

next row up:
1. init [1] * n
2. cur_row[i] = cur_row[i + 1] + prev_row[i]
3. prev_row = cur_row
4. end return cur_row[0] which is matrix[0][0]

NB - this is the same approach but cleaner.

Beat 74% run, 90% memory. 
