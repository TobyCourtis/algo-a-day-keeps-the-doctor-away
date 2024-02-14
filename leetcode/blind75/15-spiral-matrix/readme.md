Attempt:

1. init 4 pointers, left, right, top, bottom
   2. left = 0
   3. right = len(matrix[0])
   4. top = 0
   5. bottom = len(matrix)
6. Go left to right, add each elem to out. Increment top
7. Go top to bottom, add each elem to out. Decrement right
8. Go right to left, add each elem to out. Decrement bottom
9. Go bottom to top, add each elem to out. Increment left

Do all this while left < right and top < bottom. 

return out


Runtime beat 98%, memory beat 92%