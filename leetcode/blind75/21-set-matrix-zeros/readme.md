Attempt 1 (O(m + n)):

Better than making a copy of the matrix, altering the copy and then copying back to original object (hence O(m + n)
space complexity, not O(m * n)).

1. Create rows and columns set.
2. Loop through each cell in matrix
3. If cell == 0 add row index to rows set, col index to cols set
4. Loop though each cell in matrix again
5. If row in rows set or col in cols set, set cell to 0

attempt 2 (O(1) space complexity):

Same as attempt 1 but row 0 records if the corresponding columns should be set to zero and col 0 records if the
corresponding rows should be set to zero.

for 3 * 3 matrix, first row == length 3, first col = length 2

We store one extra piece of information in variable 'first_row' which records if first row should be zeroed or not. This
is required because matrix[0][0] overlaps both arrays. We use [0][0] as column 0 indicator and first_row as row
indicator.

Runtime beat 76%, memory 54%

