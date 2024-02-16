Attempt:


Case word='pow'

1. loop through all values in matrix
2. we find "p" 
3. While word not found:
   4. if up/down/right/left == "o" then increment index and repeat for "w"
   5. else: break and continue step 1
   6. if full length word found, return True
6. If all values in matrix iterated through with no word found - return False

Case I didn't consider - If all surrounding values to "p" are "o" we need to try them ALL


Attempt 2 (explore all options):

Recursively visit all neighbors, if one path of cells == word then return True.

If all paths for all cells in matrix do not return True, then return False


Runtime beat 67%, memory 61%