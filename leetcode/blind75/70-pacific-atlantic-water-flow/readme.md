attempt:

Attempted a dfs() from each cell on the grid (with caching.)

We recursively go left or right or up or down, if the correspondong next cell is LTE current cell.

Had an issue with the 'path' accumulator and the code was long/complex.



Neetcode (dfs from ocean to all cells that can reach it rather than all cells to ocean):

Intuitive, more efficient even though still O(n * m). 

One reason it's more efficient is because every cell we begin from is a valid cell (it's at the ocean), we do not needlessly visit every cell in the matrix.

It's simpler because every step of the way we are adding to a valid 'can reach the ocean' set, rather than building a path which is eventually added iff we reach the ocean.

1. Find cells that can reach pacific (using reverse dfs())
2. Find cells that can reach atlantic (same again)
3. return intersection


Beats 99% runtime, 90% memory

